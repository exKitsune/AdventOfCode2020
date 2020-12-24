from collections import deque
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

current_seats = input_file
height = len(input_file)
width = len(input_file[0])

def countAdjOccupied(seats, h, w):
    o_seats = 0
    for i in reversed(range(0, h)): # N
        if seats[i][w] == '#':
            o_seats += 1
            break
        elif seats[i][w] == 'L':
            break
    
    for i in range(h + 1, height): # S
        if seats[i][w] == '#':
            o_seats += 1
            break
        elif seats[i][w] == 'L':
            break
    
    for j in reversed(range(0, w)): # W
        if seats[h][j] == '#':
            o_seats += 1
            break
        elif seats[h][j] == 'L':
            break
    
    for j in range(w + 1, width): # E
        if seats[h][j] == '#':
            o_seats += 1
            break
        elif seats[h][j] == 'L':
            break
    
    x = h - 1
    y = w - 1
    while True: # NW        
        if x < 0 or y < 0:
            break

        if seats[x][y] == '#':
            o_seats += 1
            break
        elif seats[x][y] == 'L':
            break
        x = x - 1
        y = y - 1

    x = h - 1
    y = w + 1
    while True: # NE        
        if x < 0 or y >= width:
            break

        if seats[x][y] == '#':
            o_seats += 1
            break
        elif seats[x][y] == 'L':
            break
        x = x - 1
        y = y + 1
    
    x = h + 1
    y = w - 1
    while True: # SW
        if x >= height or y < 0:
            break

        if seats[x][y] == '#':
            o_seats += 1
            break
        elif seats[x][y] == 'L':
            break
        x = x + 1
        y = y - 1
    
    x = h + 1
    y = w + 1
    while True: # SE        
        if x >= height or y >= width:
            break

        if seats[x][y] == '#':
            o_seats += 1
            break
        elif seats[x][y] == 'L':
            break
        x = x + 1
        y = y + 1

    
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
                if countAdjOccupied(current_seats, i, j) >= 5:
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