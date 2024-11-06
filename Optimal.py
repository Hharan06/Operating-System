class OptimalPageReplacement:
    def __init__(self, capacity):
        """
        Initializes the Optimal Page Replacement algorithm with a fixed capacity.
        :param capacity: Number of frames in memory (capacity of the queue).
        """
        self.capacity = capacity
        self.memory = []  # List to store the pages in memory
        self.page_faults = 0

    def insert_page(self, page, future_requests):
        """
        Insert a page into the memory using Optimal page replacement strategy.
        :param page: The page number to be loaded into memory.
        :param future_requests: List of future page requests.
        """
        if page not in self.memory:
            # Page fault occurs if the page is not in memory
            if len(self.memory) < self.capacity:
                self.memory.append(page)
            else:
                # Find the optimal page to replace
                optimal_page = self.find_optimal_page(page, future_requests)
                print(f"Page {optimal_page} is removed (Optimal).")
                # Replace the optimal page with the new page
                self.memory.remove(optimal_page)
                self.memory.append(page)
            self.page_faults += 1
            print(f"Page {page} loaded. Memory state: {self.memory}")
        else:
            print(f"Page {page} is already in memory. No page fault. Memory state: {self.memory}")

    def find_optimal_page(self, page, future_requests):
        """
        Determines which page to replace using the Optimal algorithm.
        :param page: The page to be loaded into memory.
        :param future_requests: List of future page requests.
        :return: The page to be removed.
        """
        farthest_index = -1
        optimal_page = None
        
        for current_page in self.memory:
            try:
                # Find the index of the current page in future requests
                index = future_requests.index(current_page)
            except ValueError:
                # If the page is not found in future requests, consider it for replacement
                return current_page
            
            if index > farthest_index:
                farthest_index = index
                optimal_page = current_page

        return optimal_page

    def get_page_faults(self):
        """
        Returns the total number of page faults that occurred.
        """
        return self.page_faults

# Example usage
if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3  # Number of frames in memory

    optimal = OptimalPageReplacement(capacity)
    
    for i, page in enumerate(pages):
        # Pass the remaining future requests for the optimal decision
        optimal.insert_page(page, pages[i+1:])

    print(f"\nTotal page faults: {optimal.get_page_faults()}")
