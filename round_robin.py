class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1  # Initially set to -1 to mark when it first gets CPU time

def round_robin(processes, n, quantum):
    current_time = 0
    process_completed = 0

    print("Execution Order: ", end="")

    while process_completed < n:
        idle = True  # Flag to check if the CPU is idle

        for process in processes:
            if process.arrival_time <= current_time and process.remaining_time > 0:
                idle = False  # CPU is not idle as a process is executing

                if process.remaining_time > quantum:
                    # Process runs for a quantum time
                    if process.response_time == -1:
                        process.response_time = current_time - process.arrival_time

                    print(f"P{process.pid}", end=" ")
                    current_time += quantum
                    process.remaining_time -= quantum
                    
                else:
                    # Process runs and completes
                    if process.response_time == -1:
                        process.response_time = current_time - process.arrival_time

                    print(f"P{process.pid}", end=" ")
                    current_time += process.remaining_time
                    process.remaining_time = 0
                    process.completion_time = current_time
                    process_completed += 1

        if idle:
            # If no process is ready, increment time (CPU idle)
            print("Idle", end=" ")
            current_time += 1

    print("\n")
    
    # Calculate total waiting time and turnaround time
    total_wt = 0
    total_tat = 0
    for process in processes:
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        total_wt += process.waiting_time
        total_tat += process.turnaround_time

        # Print process details
        print(f"P{process.pid}\tArrival: {process.arrival_time}\tBurst: {process.burst_time}\tCompletion: {process.completion_time}\tTurnaround: {process.turnaround_time}\tWaiting: {process.waiting_time}")

    # Print average times
    print(f"Average Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")

def main():
    # Define processes directly in the code
    processes = [
        Process(1, 0, 10),  # Process 1: arrival time = 0, burst time = 10
        Process(2, 2, 4),   # Process 2: arrival time = 2, burst time = 4
        Process(3, 4, 6),   # Process 3: arrival time = 4, burst time = 6
        Process(4, 6, 8)    # Process 4: arrival time = 6, burst time = 8
    ]
    n = len(processes)
    quantum = 5  # Time quantum for Round Robin

    round_robin(processes, n, quantum)

if __name__ == "__main__":
    main()

