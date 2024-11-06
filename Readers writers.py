import threading
import time
import random

class ReadWriteLock:
    def __init__(self):
        self.read_lock = threading.Semaphore()  # Semaphore to allow multiple readers
        self.write_lock = threading.Semaphore(1)  # Semaphore for a single writer
        self.reader_count = 0  # Tracks the number of active readers
        self.reader_count_lock = threading.Lock()  # Lock to protect the reader count

    def acquire_read_lock(self):
        # Protect reader count update with a lock
        with self.reader_count_lock:
            self.reader_count += 1
            if self.reader_count == 1:
                self.write_lock.acquire()  # First reader locks the writer out

    def release_read_lock(self):
        # Protect reader count update with a lock
        with self.reader_count_lock:
            self.reader_count -= 1
            if self.reader_count == 0:
                self.write_lock.release()  # Last reader releases the write lock

    def acquire_write_lock(self):
        self.write_lock.acquire()  # Only one writer can enter

    def release_write_lock(self):
        self.write_lock.release()  # Release after writing


# Reader class simulates a reader thread with limited reads
class Reader(threading.Thread):
    def __init__(self, reader_id, rw_lock, max_reads):
        super().__init__()
        self.reader_id = reader_id
        self.rw_lock = rw_lock
        self.max_reads = max_reads  # Maximum number of times this reader can read
        self.read_count = 0

    def run(self):
        while self.read_count < self.max_reads:
            # Simulate time between reading
            time.sleep(random.uniform(1, 3))
            # Acquire read lock
            self.rw_lock.acquire_read_lock()
            print(f"Reader {self.reader_id} is reading.")
            time.sleep(random.uniform(0.5, 1.5))  # Simulate reading time
            print(f"Reader {self.reader_id} has finished reading.")
            # Release read lock
            self.rw_lock.release_read_lock()
            self.read_count += 1

        print(f"Reader {self.reader_id} completed {self.read_count} reads and is done.")


# Writer class simulates a writer thread with limited writes
class Writer(threading.Thread):
    def __init__(self, writer_id, rw_lock, max_writes):
        super().__init__()
        self.writer_id = writer_id
        self.rw_lock = rw_lock
        self.max_writes = max_writes  # Maximum number of times this writer can write
        self.write_count = 0

    def run(self):
        while self.write_count < self.max_writes:
            # Simulate time between writing
            time.sleep(random.uniform(2, 4))
            # Acquire write lock
            self.rw_lock.acquire_write_lock()
            print(f"Writer {self.writer_id} is writing.")
            time.sleep(random.uniform(1, 2))  # Simulate writing time
            print(f"Writer {self.writer_id} has finished writing.")
            # Release write lock
            self.rw_lock.release_write_lock()
            self.write_count += 1

        print(f"Writer {self.writer_id} completed {self.write_count} writes and is done.")


# Main class to run the Readers-Writers Problem simulation with limited steps
class ReadersWritersSimulation:
    def __init__(self, num_readers, num_writers, max_reads, max_writes):
        self.rw_lock = ReadWriteLock()
        self.readers = [Reader(i, self.rw_lock, max_reads) for i in range(num_readers)]
        self.writers = [Writer(i, self.rw_lock, max_writes) for i in range(num_writers)]

    def start_simulation(self):
        print("Starting Readers-Writers Simulation with limited steps...")
        for reader in self.readers:
            reader.start()  # Start each reader thread

        for writer in self.writers:
            writer.start()  # Start each writer thread

        # Join all threads to keep the main program running until completion
        for reader in self.readers:
            reader.join()

        for writer in self.writers:
            writer.join()

        print("Readers-Writers Simulation complete.")


# Main execution
if __name__ == "__main__":
    num_readers = 5
    num_writers = 2
    max_reads = 3  # Each reader reads a maximum of 3 times
    max_writes = 2  # Each writer writes a maximum of 2 times

    simulation = ReadersWritersSimulation(num_readers, num_writers, max_reads, max_writes)
    simulation.start_simulation()