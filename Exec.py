import os
import sys

def execute_command(command):
    try:
        # Fork the current process
        pid = os.fork()

        if pid == 0:  # Child process
            os.execvp(command[0], command)  # Replace child process with the command
            # If execvp fails
            print(f"Failed to execute command: {command[0]}", file=sys.stderr)
            sys.exit(1)
        else:  # Parent process
            # Wait for the child process to complete
            os.wait()
            print(f"Command '{' '.join(command)}' executed in child process.")

    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    commands = [
        ["ls", "-l"],
        ["pwd"],
        ["echo", "Hello World"],
    ]

    for cmd in commands:
        execute_command(cmd)

