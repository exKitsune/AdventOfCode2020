with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

group_list = []
current_group = {}
for line in input_file:
    if line == '':
        group_list.append(current_group)
        current_group = {}
    else:
        for question in line:
            current_group[question] = 1
group_list.append(current_group)

total = 0
for group in group_list:
    for value in group.values():
        total += value

print(total)