class Process:
    def __init__(self, no, arrival_time, burst_time):
        self.no = no
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.ct = 0
        self.tat = 0
        self.wt = 0

def fcfs_scheduling(processes, n):
    current_time = 0
    avgtat = 0
    avgwt = 0

    print("\nProcessNo\tArrival Time\tBurst Time\tCT\tTAT\tWT")

    for i in range(n):
        current_time += processes[i].burst_time
        processes[i].ct = current_time
        processes[i].tat = processes[i].ct - processes[i].arrival_time
        avgtat += processes[i].tat
        processes[i].wt = processes[i].tat - processes[i].burst_time
        avgwt += processes[i].wt
        print(f"P{processes[i].no}\t\t{processes[i].arrival_time}\t\t{processes[i].burst_time}\t\t{processes[i].ct}\t{processes[i].tat}\t{processes[i].wt}")

    avgtat /= n
    avgwt /= n
    print(f"\nAverage TurnAroundTime = {avgtat}\nAverage WaitingTime = {avgwt}")

def main_fcfs():
    processes = [
        Process(1, 0, 5),
        Process(2, 1, 9),
        Process(3, 2, 6),
        Process(4, 3, 7)
    ]  # Declaring processes with arrival time and burst time
    n = len(processes)

    fcfs_scheduling(processes, n)

if __name__ == "__main__":
    main_fcfs()

