import socket
import pickle

# Server configuration
host = '127.0.0.1'  # Localhost
port = 12345  # Port to listen on

def main():
    # Create and bind the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        print(f"Server listening on {host}:{port}")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            
            # Receive the serialized right half data
            right_data = b""
            while True:
                chunk = conn.recv(1024)
                if not chunk:
                    break
                right_data += chunk
            
            # Deserialize the right half data
            right_half = pickle.loads(right_data)
            print(f"Received right half of the array: {right_half}")
            
            # Compute the sum of the right half
            right_sum = sum(right_half)
            print(f"Sum of the right half: {right_sum}")

if __name__ == "__main__":
    main()

