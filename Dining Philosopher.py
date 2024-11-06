import threading
import time
import random

# Constants
NUM_PHILOSOPHERS = 5
MAX_EATING_TIMES = 3  # Each philosopher eats up to 3 times before stopping

# Class to represent each Philosopher
class Philosopher(threading.Thread):
    def __init__(self, philosopher_id, left_fork, right_fork, max_eating_times):
        super().__init__()
        self.philosopher_id = philosopher_id
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.max_eating_times = max_eating_times
        self.eating_count = 0

    def run(self):
        # Each philosopher alternates between thinking and eating
        while self.eating_count < self.max_eating_times:
            self.think()
            self.eat()

        print(f"Philosopher {self.philosopher_id} has finished eating {self.eating_count} times and is done.")

    def think(self):
        print(f"Philosopher {self.philosopher_id} is thinking.")
        time.sleep(random.uniform(1, 2))  # Random time spent thinking

    def eat(self):
        # Try to pick up both forks
        print(f"Philosopher {self.philosopher_id} is hungry and attempting to pick up forks.")
        with self.left_fork:
            print(f"Philosopher {self.philosopher_id} picked up left fork.")
            with self.right_fork:
                print(f"Philosopher {self.philosopher_id} picked up right fork.")
                # At this point, the philosopher has both forks and can eat
                print(f"Philosopher {self.philosopher_id} is eating.")
                time.sleep(random.uniform(1, 2))  # Random time spent eating
                self.eating_count += 1  # Increase the eating count

        # After eating, forks are automatically released due to `with` context
        print(f"Philosopher {self.philosopher_id} finished eating and released both forks.")

# Class to set up and manage the Dining Philosophers simulation
class DiningPhilosophers:
    def __init__(self, num_philosophers, max_eating_times):
        self.num_philosophers = num_philosophers
        self.max_eating_times = max_eating_times
        # Create a list of semaphores, each representing a fork
        self.forks = [threading.Semaphore(1) for _ in range(num_philosophers)]
        # Create philosophers with appropriate left and right forks and max eating times
        self.philosophers = [
            Philosopher(i, self.forks[i], self.forks[(i + 1) % num_philosophers], self.max_eating_times)
            for i in range(num_philosophers)
        ]

    def start_dining(self):
        print("Starting the Dining Philosophers simulation...")
        for philosopher in self.philosophers:
            philosopher.start()  # Start each philosopher's thread

        for philosopher in self.philosophers:
            philosopher.join()  # Wait for each philosopher thread to complete

# Main code to execute the Dining Philosophers problem
if __name__ == "__main__":
    dining_philosophers = DiningPhilosophers(NUM_PHILOSOPHERS, MAX_EATING_TIMES)
    dining_philosophers.start_dining()
    print("Dining Philosophers simulation complete.")