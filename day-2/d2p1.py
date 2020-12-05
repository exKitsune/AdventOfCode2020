with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

total_valid = 0
for line in input_file:
    cut = line.index("-")
    min_num = int(line[:cut])
    line = line[cut + 1:]

    cut = line.index(' ')
    max_num = int(line[:cut])
    line = line[cut + 1:]

    cut = line.index(':')
    char = line[:cut]
    line = line[cut + 2:]

    password = line

    count = password.count(char)
    if count >= min_num and count <= max_num:
        total_valid += 1

print(total_valid)

