from collections import deque
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

numbers = deque()
for line in input_file:
    numbers.append(int(line))

k_group = deque()
for i in range(0, 25):
    k_group.append(numbers.popleft())

for num in numbers:
    k_pairs = []
    for i in range(0, len(k_group) - 1):
        working_list = list(k_group)
        for k in working_list[i+1:]:
            k_pairs.append(k_group[i] + k)
    
    if num not in k_pairs:
        print(num)
        break

    k_group.popleft()
    k_group.append(num)


