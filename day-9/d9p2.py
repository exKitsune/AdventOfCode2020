from collections import deque
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

numbers = deque()
for line in input_file:
    numbers.append(int(line))

the_number = 756008079 #from part 1

found = False
start_index = 0
end_index = 2
working_list = []
while not found:
    running_sum = 0
    working_list = []
    for i in range(start_index, end_index):
        running_sum += numbers[i]
        working_list.append(numbers[i])
    
    if running_sum < the_number:
        end_index += 1
    elif running_sum > the_number:
        start_index += 1
        end_index = start_index + 2
    else:
        found = True

print(min(working_list) + max(working_list))