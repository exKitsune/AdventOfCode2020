with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

highest = 0
#BFBBBBBLLR is example line
#for line in input_file:
for line in input_file:
    current_row = 0b01111111
    current_col = 0b0111
    row_step = 0b01000000
    col_step = 0b0100

    for char in line:
        if char == 'F':
            current_row = current_row & (0b11111111 - row_step)
            row_step = row_step >> 1
        elif char == 'B':
            current_row = current_row | row_step
            row_step = row_step >> 1
        elif char == 'L':
            current_col = current_col & (0b11111111 - col_step)
            col_step = col_step >> 1
        elif char == 'R':
            current_col = current_col | col_step
            col_step = col_step >> 1
        #print(char, current_row, current_col, row_step, col_step)
    value = int(current_row) * 8 + int(current_col)
    highest = max(value, highest)

print(highest)