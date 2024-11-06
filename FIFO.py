from collections import deque

class FIFOPageReplacement:
    def __init__(self, capacity):
        """
        Initializes the FIFO Page Replacement algorithm with a fixed capacity.
        :param capacity: Number of frames in memory (capacity of the queue).
        """
        self.capacity = capacity
        self.memory = deque(maxlen=capacity)  # Queue for FIFO page replacement
        self.page_faults = 0

    def insert_page(self, page):
        """
        Insert a page into the memory using FIFO page replacement strategy.
        :param page: The page number to be loaded into memory.
        """
        if page not in self.memory:
            # Page fault occurs if the page is not in memory
            if len(self.memory) == self.capacity:
                print(f"Page {self.memory[0]} is removed.")
            self.memory.append(page)
            self.page_faults += 1
            print(f"Page {page} loaded. Memory state: {list(self.memory)}")
        else:
            print(f"Page {page} is already in memory. No page fault. Memory state: {list(self.memory)}")

    def get_page_faults(self):
        """
        Returns the total number of page faults that occurred.
        """
        return self.page_faults

# Example usage
if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3  # Number of frames in memory

    fifo = FIFOPageReplacement(capacity)
    
    for page in pages:
        fifo.insert_page(page)
    
    print(f"\nTotal page faults: {fifo.get_page_faults()}")