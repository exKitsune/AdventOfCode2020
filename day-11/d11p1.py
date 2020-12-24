from collections import deque
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

current_seats = input_file
height = len(input_file)
width = len(input_file[0])

def countAdjOccupied(seats, h, w):
    o_seats = 0
    for i in range(h-1,h+2):
        for j in range(w-1,w+2):
            if i < 0 or i >= height or j < 0 or j >= width or (i == h and j == w):
                continue
            else:
                if seats[i][j] == '#':
                    o_seats += 1
    
    return o_seats

while True:
    next_seats = []

    for i in range(0, height):
        current_row = ""
        for j in range(0, width):
            if current_seats[i][j] == 'L':
                if countAdjOccupied(current_seats, i, j) == 0:
                    current_row += "#"
                else:
                    current_row += "L"
            elif current_seats[i][j] == '#':
                if countAdjOccupied(current_seats, i, j) >= 4:
                    current_row += "L"
                else:
                    current_row += "#"
            else:
                current_row += "."
        next_seats.append(current_row)

    if current_seats == next_seats:
        break
    current_seats = next_seats

print("".join(current_seats).count("#"))