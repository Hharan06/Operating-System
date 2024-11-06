import socket
import sysv_ipc 

host = "127.0.0.1"
port = 2468

def server_write():
    key = 1234
    shm = sysv_ipc.SharedMemory(key, sysv_ipc.IPC_CREAT, 0o666, 1024)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server is listening for connections...")
        
        conn, addr = s.accept()
        
        with conn:
            print(f"Connected by {addr}")
            message = input('Enter data to write into shared memory: ')
            shm.write(message.encode())
            print('Data written to memory')
            
            # Send an acknowledgment to the client
            conn.sendall(b'Data written')

            shm.detach()

if __name__ == "__main__":
    server_write()

