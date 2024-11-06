import os
import socket
import pickle

# Define the array and split it
array = [1, 2, 3, 4, 5, 6, 7, 8]
mid = len(array) // 2  
left = array[:mid]
right = array[mid:]

# Initialize sums
left_sum = 0

# Fork the process
process_id = os.fork()

if process_id > 0:
    # Parent process
    print('Parent process started')
    
    # Compute sum of the left half
    left_sum = sum(left)
    print("Parent process: Sum of the left half =", left_sum)
    
    # Wait for the child process to finish
    os.wait()

elif process_id == 0:
    # Child process
    print('Child process started')
    
    server_ip = '127.0.0.1'  # Localhost
    server_port = 12345
    
    right_data = pickle.dumps(right)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((server_ip, server_port))
            s.sendall(right_data)
        except ConnectionRefusedError:
            print("Connection refused. Ensure the server is running and the IP/port are correct.")
    
    # Exit the child process
    os._exit(0)

