class MemoryAllocator:
    def __init__(self, memory_blocks):
        """
        :param memory_blocks: List of available memory block sizes.
        """
        self.memory_blocks = memory_blocks

    def first_fit(self, process_size):
        """
        First Fit Allocation: Finds the first block that is large enough for the process.
        :param process_size: Size of the memory required by the process.
        :return: Index of the allocated block or -1 if allocation failed.
        """
        for i, block in enumerate(self.memory_blocks):
            if block >= process_size:
                print(f"Allocating {process_size} to block of size {block} (First Fit).")
                self.memory_blocks[i] -= process_size
                return i
        print(f"First Fit: No block large enough for {process_size}.")
        return -1

    def best_fit(self, process_size):
        """
        Best Fit Allocation: Finds the smallest block that is large enough for the process.
        :param process_size: Size of the memory required by the process.
        :return: Index of the allocated block or -1 if allocation failed.
        """
        best_index = -1
        best_fit = float('inf')
        
        for i, block in enumerate(self.memory_blocks):
            if block >= process_size and (block - process_size) < best_fit:
                best_fit = block - process_size
                best_index = i

        if best_index != -1:
            print(f"Allocating {process_size} to block of size {self.memory_blocks[best_index]} (Best Fit).")
            self.memory_blocks[best_index] -= process_size
        else:
            print(f"Best Fit: No block large enough for {process_size}.")
        
        return best_index

    def worst_fit(self, process_size):
        """
        Worst Fit Allocation: Finds the largest block to allocate the process.
        :param process_size: Size of the memory required by the process.
        :return: Index of the allocated block or -1 if allocation failed.
        """
        worst_index = -1
        worst_fit = -1
        
        for i, block in enumerate(self.memory_blocks):
            if block >= process_size and (block - process_size) > worst_fit:
                worst_fit = block - process_size
                worst_index = i

        if worst_index != -1:
            print(f"Allocating {process_size} to block of size {self.memory_blocks[worst_index]} (Worst Fit).")
            self.memory_blocks[worst_index] -= process_size
        else:
            print(f"Worst Fit: No block large enough for {process_size}.")
        
        return worst_index

    def reset_memory(self, memory_blocks):
        """
        Resets the memory blocks to the initial configuration.
        :param memory_blocks: New list of available memory block sizes.
        """
        self.memory_blocks = memory_blocks
        print("Memory blocks have been reset.")


# Example usage
if __name__ == "__main__":
    initial_memory_blocks = [100, 500, 200, 300, 600]  # Available memory blocks
    allocator = MemoryAllocator(initial_memory_blocks)

    # Process sizes to allocate
    processes = [212, 417, 112, 426]

    print("First Fit Allocation:")
    allocator.reset_memory(initial_memory_blocks.copy())
    for process in processes:
        allocator.first_fit(process)

    print("\nBest Fit Allocation:")
    allocator.reset_memory(initial_memory_blocks.copy())
    for process in processes:
        allocator.best_fit(process)

    print("\nWorst Fit Allocation:")
    allocator.reset_memory(initial_memory_blocks.copy())
    for process in processes:
        allocator.worst_fit(process)