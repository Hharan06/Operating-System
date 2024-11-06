import os

def child(pipe_out):
    """
    Child process function to send data through the pipe.
    """
    print("Child process is writing to pipe...")
    message = "Hello from the child process!"
    os.write(pipe_out, message.encode())  # Write message to pipe
    os.close(pipe_out)  # Close the write-end of the pipe after sending the message

def parent(pipe_in):
    """
    Parent process function to read data from the pipe.
    """
    print("Parent process is reading from pipe...")
    message = os.read(pipe_in, 1024).decode()  # Read from pipe
    print(f"Parent received: {message}")
    os.close(pipe_in)  # Close the read-end of the pipe after reading the message

def main():
    # Create a pipe
    pipe_in, pipe_out = os.pipe()  # pipe_in is the read end, pipe_out is the write end

    pid = os.fork()  # Create a new child process

    if pid == 0:
        # This is the child process
        os.close(pipe_in)  # Close the read end in the child
        child(pipe_out)
    else:
        # This is the parent process
        os.close(pipe_out)  # Close the write end in the parent
        parent(pipe_in)

if __name__ == "__main__":
    main()

