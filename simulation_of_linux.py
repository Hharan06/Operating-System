import subprocess
import time

def simulate_cat(file_path, redirect=None, append=False):
    """Simulate the `cat` command with optional redirection."""
    mode = 'a' if append else 'w'

    with open(file_path, 'r') as f:
        content = f.read()

    if redirect:
        with open(redirect, mode) as out_f:
            out_f.write(content)
        print(f'Content redirected to {redirect}')
    else:
        print(content)

def simulate_ps(*args):
    """Simulate the `ps` command."""
    result = subprocess.run(['ps', *args], text=True, capture_output=True)
    print(result.stdout)


simulate_cat('sample.txt', 'output.txt')  # Overwrite
simulate_cat('sample.txt', 'output.txt', append=True)  # Append
simulate_ps('-aux')

