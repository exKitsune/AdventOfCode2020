with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

list_2 = []
for i in input_file:
    list_2.append(2020 - int(i))

dupe_numbers = []
for i in list_2:
    if str(i) in input_file:
        dupe_numbers.append(i)

answer = 1
for i in dupe_numbers:
    answer *= i

print(answer)