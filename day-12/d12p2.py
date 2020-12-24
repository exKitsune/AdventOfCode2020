from collections import deque
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

(x, y) = (0, 0)
(w_x, w_y) = (10, 1)
(n_x, n_y) = (0, 0)
for line in input_file:
    num = int(line[1:])
    if line.startswith("N"):
        w_y += num
    elif line.startswith("S"):
        w_y -= num
    elif line.startswith("W"):
        w_x -= num
    elif line.startswith("E"):
        w_x += num
    elif line.startswith("R"):
        if num == 90:
            n_x = w_y
            n_y = -w_x
        elif num == 180:
            n_x = -w_x
            n_y = -w_y
        elif num == 270:
            n_x = -w_y
            n_y = w_x
        else:
            n_x = w_x
            n_y = w_y
        w_x = n_x
        w_y = n_y
    elif line.startswith("L"):
        if num == 90:
            n_x = -w_y
            n_y = w_x
        elif num == 180:
            n_x = -w_x
            n_y = -w_y
        elif num == 270:
            n_x = w_y
            n_y = -w_x
        else:
            n_x = w_x
            n_y = w_y
        w_x = n_x
        w_y = n_y
    elif line.startswith("F"):
        for i in range(0, num):
            x += w_x
            y += w_y

print(abs(x) + abs(y))