from collections import deque
import math

def cnt_arg(n):
    paths = [1, 1, 2, 4]
    if n <= 2:
        return paths[n]
    
    for i in range(3, n):
        paths.append(paths[i] + paths[i-1] + paths[i-2])
    
    return paths[-1]

with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

numbers = []
for line in input_file:
    numbers.append(int(line))

numbers.sort()
current_volt = 0
#jumps = [0, 0, 0, 1] # 0 volt jumps, 1 volt jumps, 2 etc

sum_arrange = 1
chain = 0
for num in numbers:
    diff = num - current_volt
    
    if diff == 1:
        chain += 1

    elif diff == 3: 
        sum_arrange *= cnt_arg(chain) 
        chain = 0

    current_volt = num

sum_arrange *= cnt_arg(chain)

#print(numbers)
print(sum_arrange)

'''
0 

0 1 

0 1 2
0 2

0 1 2 3 
0 3 
0 1 3 
0 2 3 

0 1 2 3 4 
0 3 4 
0 1 3 4
0 2 3 4
0 1 4 
0 1 2 4 
0 2 4 

0 1 2 3 4 5
0 1 3 4 5
0 2 3 4 5
0 3 4 5
0 1 4 5
0 1 2 4 5
0 2 4 5
0 1 2 5
0 2 5
0 3 5
0 1 3 5
0 2 3 5
0 1 2 3 5
'''