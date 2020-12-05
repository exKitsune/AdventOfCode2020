with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

snow = '.'
tree = '#'

num_trees_hit = 0
x = 0
y = 0

list_d = [ 
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

result = 1
repeat_width = len(input_file[0])
end = len(input_file)
for (dx, dy) in list_d:
    x, y = (0, 0)
    num_trees_hit = 0
    while y < end:
        
        if input_file[y][x % repeat_width] == tree:
            num_trees_hit += 1

        x += dx
        y += dy
    
    result *= num_trees_hit

print(result)