from collections import deque
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

(x, y) = (0, 0)
angle = 0 #0 east, 90 north, 180 west, 270 south
for line in input_file:
    num = int(line[1:])
    if line.startswith("N"):
        y += num
    elif line.startswith("S"):
        y -= num
    elif line.startswith("W"):
        x -= num
    elif line.startswith("E"):
        x += num
    elif line.startswith("R"):
        angle = (angle - num) % 360
    elif line.startswith("L"):
        angle = (angle + num) % 360
    elif line.startswith("F"):
        if angle == 0:
            x += num
        elif angle == 90:
            y += num
        elif angle == 180:
            x -= num
        elif angle == 270:
            y -= num

print(abs(x) + abs(y))