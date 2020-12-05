with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

snow = '.'
tree = '#'

num_trees_hit = 0
x = 0
y = 0
dx = 3
dy = 1

repeat_width = len(input_file[0])
end = len(input_file)
while y < end:
    
    if input_file[y][x % repeat_width] == tree:
        num_trees_hit += 1

    x += dx
    y += dy

print(num_trees_hit)