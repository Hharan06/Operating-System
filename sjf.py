class Process:
    def __init__(self, pid, arrival_time, burst_time):  
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = 0

def display_gantt_chart(processes, n):
    print("\nGantt Chart:")
    for p in processes:
        print(f"P{p.pid}", end=" -> ")
    print("End")

def sjf_np(processes, n):
    avg_wt = 0
    avg_tat = 0
    avg_rt = 0

    # Sort processes based on arrival time
    processes.sort(key=lambda x: x.arrival_time)

    current_time = 0

    print("Process\tArrival time\tBurst time\tCompletion time\tTurnaround Time\tWaiting time\tResponse time")

    for i in range(n):
        # Find the next process to execute (with the shortest burst time and has arrived)
        min_index = i
        for j in range(i + 1, n):
            if processes[j].arrival_time <= current_time and processes[j].burst_time < processes[min_index].burst_time:
                min_index = j

        # Swap the selected process with the current one
        processes[i], processes[min_index] = processes[min_index], processes[i]

        current_time += processes[i].burst_time
        processes[i].completion_time = current_time 
        processes[i].turnaround_time = processes[i].completion_time - processes[i].arrival_time
        processes[i].waiting_time = processes[i].turnaround_time - processes[i].burst_time
        processes[i].response_time = processes[i].waiting_time

        avg_wt += processes[i].waiting_time
        avg_tat += processes[i].turnaround_time
        avg_rt += processes[i].response_time


        # Display process details
        print(f"P{processes[i].pid}\t\t{processes[i].arrival_time}\t\t{processes[i].burst_time}\t\t{processes[i].completion_time}\t\t{processes[i].turnaround_time}\t\t{processes[i].waiting_time}\t\t{processes[i].response_time}")

    # Calculate averages
    avg_wt /= n
    avg_tat /= n
    avg_rt /= n

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Average Response Time: {avg_rt:.2f}")

    # Display Gantt chart
    display_gantt_chart(processes,n)

# Define default processes (no input required)
processes = [
    Process(1, 0, 8),
    Process(2, 1, 9),
    Process(3, 2, 9),
    Process(4, 3, 5)
]

n = len(processes)

# Run the SJF Non-Preemptive scheduler
sjf_np(processes, n)

