class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1  # -1 means the process has not started yet

def sjf_preemptive(processes, n):
    current_time = 0
    completed = 0
    min_burst_idx = -1
    shortest_remaining_time = float('inf')
    is_process_running = False
    total_wt = 0
    total_tat = 0
    total_rt = 0

    while completed != n:
        # Find the process with the shortest remaining time at current time
        for i in range(n):
            if processes[i].arrival_time <= current_time and processes[i].remaining_time > 0:
                if processes[i].remaining_time < shortest_remaining_time:
                    shortest_remaining_time = processes[i].remaining_time
                    min_burst_idx = i
                    is_process_running = True
                elif processes[i].remaining_time == shortest_remaining_time:
                    if processes[i].arrival_time < processes[min_burst_idx].arrival_time:
                        min_burst_idx = i
        
        if not is_process_running:  # No process is available at this time
            current_time += 1
            continue

        # Start the process if it hasn't started before
        if processes[min_burst_idx].response_time == -1:
            processes[min_burst_idx].response_time = current_time - processes[min_burst_idx].arrival_time
        
        # Process the selected one for 1 unit of time
        processes[min_burst_idx].remaining_time -= 1
        current_time += 1
        shortest_remaining_time = processes[min_burst_idx].remaining_time

        # If a process finishes execution
        if processes[min_burst_idx].remaining_time == 0:
            completed += 1
            is_process_running = False
            shortest_remaining_time = float('inf')

            processes[min_burst_idx].completion_time = current_time
            processes[min_burst_idx].turnaround_time = processes[min_burst_idx].completion_time - processes[min_burst_idx].arrival_time
            processes[min_burst_idx].waiting_time = processes[min_burst_idx].turnaround_time - processes[min_burst_idx].burst_time

            total_wt += processes[min_burst_idx].waiting_time
            total_tat += processes[min_burst_idx].turnaround_time
            total_rt += processes[min_burst_idx].response_time

    # Print the results
    print("\nP\tAT\tBT\tCT\tTAT\tWT\tRT")
    for p in processes:
        print(f"P{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.completion_time}\t{p.turnaround_time}\t{p.waiting_time}\t{p.response_time}")

    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")
    print(f"Average Response Time: {total_rt / n:.2f}")

def main_sjf_preemptive():
    processes = [
        Process(1, 0, 8),
        Process(2, 1, 4),
        Process(3, 2, 9),
        Process(4, 3, 5)
    ]  # Declaring processes with arrival time and burst time

    n = len(processes)
    sjf_preemptive(processes, n)

if __name__ == "__main__":
    main_sjf_preemptive()

