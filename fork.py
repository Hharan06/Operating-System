import os
import socket 

process_id = os.fork()
print(process_id)

array = [1, 2, 3, 4, 5, 6, 7, 8]
mid = len(array) // 2  
left = array[:mid]
right = array[mid:]

left_sum = 0
right_sum = 0


if process_id > 0:
    print('Parent process started')
    
    for i in range(len(left)):
        left_sum += left[i]
    print("Parent process: Sum of the left half = ",left_sum)

elif process_id == 0:
    print('Child process started')
    for i in range(len(right)):
        right_sum += right[i]
    print("Child process: Sum of the right half = ",right_sum)
    
