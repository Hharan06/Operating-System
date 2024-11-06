class BankersAlgorithm:
    def __init__(self, total_resources, max_demand, allocation):
        """
        :param total_resources: List of total available resources in the system.
        :param max_demand: 2D List, where each sub-list represents the maximum demand of each process.
        :param allocation: 2D List, where each sub-list represents the resources currently allocated to each process.
        """
        self.total_resources = total_resources
        self.max_demand = max_demand
        self.allocation = allocation
        self.num_processes = len(max_demand)
        self.num_resources = len(total_resources)
        self.calculate_need()
        self.available = [self.total_resources[i] - sum(self.allocation[j][i] for j in range(self.num_processes)) 
                          for i in range(self.num_resources)]
        
    def calculate_need(self):
        """
        Calculates the 'need' matrix for each process, representing remaining resource needs.
        """
        self.need = [[self.max_demand[i][j] - self.allocation[i][j] for j in range(self.num_resources)]
                     for i in range(self.num_processes)]
    
    def is_safe_state(self):
        """
        Determines if the system is in a safe state, returning the safe sequence if one exists.
        :return: (bool, List) where the bool indicates if the system is safe, and List is the safe sequence.
        """
        work = self.available[:]  # Work represents available resources at each step
        finish = [False] * self.num_processes  # Tracks if each process can finish
        safe_sequence = []
        
        while len(safe_sequence) < self.num_processes:
            found = False  # To check if at least one process can proceed
            for i in range(self.num_processes):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(self.num_resources)):
                    # Process can be allocated resources to proceed
                    for j in range(self.num_resources):
                        work[j] += self.allocation[i][j]  # Release resources
                    safe_sequence.append(i)
                    finish[i] = True
                    found = True
                    break
            
            if not found:
                return False, []  # If no process could proceed, it's an unsafe state
        
        return True, safe_sequence

    def request_resources(self, process_id, request):
        """
        Attempts to allocate requested resources to a process.
        :param process_id: ID of the process making the request.
        :param request: List of resources being requested by the process.
        :return: bool indicating if the request could be safely granted.
        """
        # Check if the request is valid
        if any(request[j] > self.need[process_id][j] for j in range(self.num_resources)):
            print("Error: Process has exceeded its maximum claim.")
            return False

        if all(request[j] <= self.available[j] for j in range(self.num_resources)):
            # Temporarily allocate resources
            for j in range(self.num_resources):
                self.available[j] -= request[j]
                self.allocation[process_id][j] += request[j]
                self.need[process_id][j] -= request[j]
            
            # Check if the system remains in a safe state
            safe, _ = self.is_safe_state()
            if safe:
                print(f"Resources allocated to process {process_id}.")
                return True
            else:
                # Rollback allocation if unsafe
                for j in range(self.num_resources):
                    self.available[j] += request[j]
                    self.allocation[process_id][j] -= request[j]
                    self.need[process_id][j] += request[j]
                print("Request would result in an unsafe state; request denied.")
                return False
        else:
            print("Resources not available for request.")
            return False

# Example usage of the Banker's Algorithm
if __name__ == "__main__":
    # Example resources and demands
    total_resources = [10, 5, 7]  # Total resources in the system
    max_demand = [
        [7, 5, 3],  # Maximum demand of process 0
        [3, 2, 2],  # Maximum demand of process 1
        [9, 0, 2],  # Maximum demand of process 2
        [2, 2, 2],  # Maximum demand of process 3
        [4, 3, 3]   # Maximum demand of process 4
    ]
    allocation = [
        [0, 1, 0],  # Resources allocated to process 0
        [2, 0, 0],  # Resources allocated to process 1
        [3, 0, 2],  # Resources allocated to process 2
        [2, 1, 1],  # Resources allocated to process 3
        [0, 0, 2]   # Resources allocated to process 4
    ]

    # Initialize the Banker's Algorithm
    banker = BankersAlgorithm(total_resources, max_demand, allocation)

    # Check if the system is in a safe state
    safe, safe_sequence = banker.is_safe_state()
    if safe:
        print("System is in a safe state.")
        print(f"Safe sequence is: {safe_sequence}")
    else:
        print("System is not in a safe state.")

    # Example request
    request = [1, 0, 2]  # Example request by process 1
    process_id = 1
    print(f"\nProcess {process_id} requesting resources: {request}")
    banker.request_resources(process_id, request)