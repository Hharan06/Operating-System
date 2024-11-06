import socket 
import sysv_ipc

host = "127.0.0.1"
port = 2468

def client_read():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        key = 1234
        shm = sysv_ipc.SharedMemory(key)

        # Wait for an acknowledgment from the server
        ack = s.recv(1024)
        if ack:
            print('Received acknowledgment from server:', ack.decode())

            # Read data from shared memory
            data = shm.read(1024).decode('utf-8').strip('\x00')
            print('Data read from shared memory:', data)
        
        shm.remove()

if __name__ == "__main__":
    client_read()

