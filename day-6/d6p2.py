with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

current_group = {}
group_size = 1
group_count = 0
for line in input_file:
    if line == '':
        for answers in current_group.values():
            if answers == group_size - 1:
                group_count += 1
        group_size = 0
        current_group = {}
    else:
        for question in line:
            try:
                prev_value = current_group[question]
            except:
                prev_value = 0
            current_group[question] = prev_value + 1
    group_size += 1

for answers in current_group.values():
    if answers == group_size - 1:
        group_count += 1
print(group_count)