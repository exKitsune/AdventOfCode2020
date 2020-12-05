with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

seats_taken = "0" * 128 * 8
seats_taken = list(seats_taken)
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
    seats_taken[current_row * 8 + current_col] = "1"

#given the assumption that there is one single free seat
flag = False
seat_id = 0
for seat in seats_taken:
    if seat == "1" and not flag:
        flag = True
    if flag and seat == "0":
        print(seat_id)
        break
    seat_id += 1

