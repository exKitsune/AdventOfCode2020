with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

total_valid = 0
for line in input_file:
    cut = line.index("-")
    first_index = int(line[:cut])
    line = line[cut + 1:]

    cut = line.index(' ')
    second_index = int(line[:cut])
    line = line[cut + 1:]

    cut = line.index(':')
    char = line[:cut]
    line = line[cut + 2:]

    password = line
    policy = password[first_index-1] + password[second_index-1]
    total_valid += policy.count(char) % 2
    

print(total_valid)