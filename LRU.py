class LRUPageReplacement:
    def __init__(self, capacity):
        """
        Initializes the LRU Page Replacement algorithm with a fixed capacity.
        :param capacity: Number of frames in memory (capacity of the queue).
        """
        self.capacity = capacity
        self.memory = []  # List to store the pages in memory
        self.page_faults = 0

    def insert_page(self, page):
        """
        Insert a page into the memory using LRU page replacement strategy.
        :param page: The page number to be loaded into memory.
        """
        if page not in self.memory:
            # Page fault occurs if the page is not in memory
            if len(self.memory) == self.capacity:
                # Remove the least recently used page
                lru_page = self.memory.pop(0)
                print(f"Page {lru_page} is removed (LRU).")
            self.memory.append(page)
            self.page_faults += 1
            print(f"Page {page} loaded. Memory state: {self.memory}")
        else:
            # Page is already in memory, update its position to most recently used
            self.memory.remove(page)
            self.memory.append(page)
            print(f"Page {page} is already in memory. Updated position. Memory state: {self.memory}")

    def get_page_faults(self):
        """
        Returns the total number of page faults that occurred.
        """
        return self.page_faults

# Example usage
if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3  # Number of frames in memory

    lru = LRUPageReplacement(capacity)
    
    for page in pages:
        lru.insert_page(page)
    
    print(f"\nTotal page faults: {lru.get_page_faults()}")
