import multiprocessing
from multiprocessing import shared_memory
import struct
import time

# Server class
class Server:
    def __init__(self, memory_name, buffer_size):
        self.buffer_size = buffer_size
        self.memory_name = memory_name
        self.shm = None

    def start(self):
        # Create a shared memory block with a specific size
        self.shm = shared_memory.SharedMemory(name=self.memory_name, create=True, size=self.buffer_size)
        print(f"Server started with shared memory name: {self.memory_name}")

        try:
            while True:
                # Reading from shared memory
                message = self.read_message()
                if message:
                    print(f"Server received: {message}")
                    # Respond by writing back a modified message
                    response = f"Server Acknowledged: {message}"
                    self.write_message(response)
                    print(f"Server sent response: {response}")
                time.sleep(1)  # Control the loop speed

        except KeyboardInterrupt:
            print("Server shutting down...")
        finally:
            # Clean up shared memory
            self.shm.close()
            self.shm.unlink()

    def read_message(self):
        # Read the raw bytes from shared memory and decode them as a string
        message_bytes = self.shm.buf[:self.buffer_size]
        message = message_bytes.tobytes().decode('utf-8').strip('\x00')
        return message if message else None

    def write_message(self, message):
        # Encode message to bytes and place it into shared memory
        message_bytes = message.encode('utf-8')
        self.shm.buf[:len(message_bytes)] = message_bytes

# Client class
class Client:
    def __init__(self, memory_name, buffer_size):
        self.buffer_size = buffer_size
        self.memory_name = memory_name
        self.shm = None

    def connect(self):
        # Connect to existing shared memory
        self.shm = shared_memory.SharedMemory(name=self.memory_name)
        print(f"Client connected to shared memory: {self.memory_name}")

    def send_message(self, message):
        # Write the message into shared memory
        print(f"Client sending: {message}")
        message_bytes = message.encode('utf-8')
        self.shm.buf[:len(message_bytes)] = message_bytes

    def receive_message(self):
        # Read the message from shared memory
        message_bytes = self.shm.buf[:self.buffer_size]
        response = message_bytes.tobytes().decode('utf-8').strip('\x00')
        print(f"Client received: {response}")
        return response

    def disconnect(self):
        # Clean up shared memory reference
        self.shm.close()

# Main code
if __name__ == "__main__":
    # Configuration
    MEMORY_NAME = "shared_memory_example"
    BUFFER_SIZE = 256

    # Start the server process
    server = Server(MEMORY_NAME, BUFFER_SIZE)  # Create Server instance
    server_process = multiprocessing.Process(target=server.start)  # Pass 'server.start' as the target function
    server_process.start()

    # Wait for the server to start
    time.sleep(1)

    # Start the client
    client = Client(MEMORY_NAME, BUFFER_SIZE)
    client.connect()
    
    try:
        # Send a message from the client
        client.send_message("Hello from Client!")
        time.sleep(1)  # Allow some time for the server to process
        
        # Receive the response from the server
        client.receive_message()

    finally:
        client.disconnect()
        server_process.terminate()