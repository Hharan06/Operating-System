import threading
import random
import time

capacity = 10
buffer_storage = [0 for i in range(capacity)]

in_index = 0
out_index = 0

mutex = threading.Semaphore()
empty = threading.Semaphore(capacity)
full = threading.Semaphore(0)

class Producer(threading.Thread):
	def run(self):
		global capacity, buffer_storage, in_index, out_index
		global mutex, empty, full
		
		items_produced = 0
		
		while items_produced < 20:
			mutex.acquire()
			empty.acquire()
			
			new_item = random.randint(1,10)
			buffer_storage[in_index] = new_item
			in_index = (in_index+1)%capacity
			print('Producer added item:',new_item)
			print('Storage:',buffer_storage)
			
			mutex.release()
			full.release()
			
			time.sleep(1)
			
			items_produced += 1
			print('Total items produced:',items_produced)
			

class Consumer(threading.Thread):
	def run(self):
		global capacity, buffer_storage, in_index, out_index
		global mutex, empty, full
		
		items_consumed = 0
		
		while items_consumed < 20:
			mutex.acquire()
			full.acquire()
			
			item = buffer_storage[out_index]
			buffer_storage[out_index] = '_'
			out_index = (out_index+1)%capacity
			print('Consumer consumed item:',item)
			print('Storage:',buffer_storage)
			
			empty.release()
			mutex.release()
			
			time.sleep(2)
			
			items_consumed += 1
			

producer = Producer()
consumer = Consumer()

producer.start()
consumer.start()

producer.join()
consumer.join()



#mutex = threading.Semaphore()

#This semaphore is initialized with a default value of 1, meaning it acts as a binary semaphore (or a mutex). It is used to ensure mutual exclusion, allowing only one thread to enter a critical section at a time.

#    mutex.acquire(): If the semaphore's counter is 1 (indicating that no thread currently holds the mutex), the counter is decremented to 0, and the thread can enter the critical section. If another thread #is holding the mutex (counter is 0), the calling thread will block until the mutex is released.
#    mutex.release(): This increments the semaphore’s counter back to 1, allowing other threads to acquire the mutex and enter the critical section.

#empty = threading.Semaphore(0)

#This semaphore is initialized with a value of 0, meaning no resources are available initially. It is used to keep track of the number of empty slots in a buffer (or similar structure).

#    empty.acquire(): This will block if the counter is 0, meaning there are no empty slots available. When there is at least one empty slot (counter > 0), acquire() will decrement the counter by 1 and allow #the thread to proceed.
#    empty.release(): This increments the counter, representing an additional empty slot, and potentially wakes up a blocked thread waiting for an empty slot.

#full = threading.Semaphore(capacity)

#This semaphore is initialized with a value equal to capacity, representing the maximum number of full slots (or items) that the buffer can hold.

#    full.acquire(): This operation will block if the counter is 0, meaning there are no full slots available. If there are full slots (counter > 0), acquire() decrements the counter by 1, allowing the #thread to proceed.
#    full.release(): This increments the counter, representing an additional full slot, and potentially wakes up a blocked thread waiting for a full slot.
