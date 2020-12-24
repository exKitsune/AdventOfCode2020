from collections import deque
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

numbers = []
for line in input_file:
    numbers.append(int(line))

numbers.sort()
current_volt = 0
jumps = [0, 0, 0, 1] # 0 volt jumps, 1 volt jumps, 2 etc

for num in numbers:
    diff = num - current_volt
    if diff > 3:
        break
    jumps[diff] += 1
    current_volt = num

print(jumps[3] * jumps[1])