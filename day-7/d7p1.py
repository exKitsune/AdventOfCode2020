import re
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

def find(query, hold_string, colors):
    nums = hold_string.split(",")[:-1:2]
    holds = hold_string.split(",")[1::2]

    if "other" in holds:
        return False
    if query in holds:
        return True
    
    else:
        has = False
        #print(holds)
        for hold in holds:
            has = has or find(query, colors[hold], colors)
        return has

colors = {}
for line in input_file:
    portions = re.split(" bags contain ", line)
    color = portions[0]
    hold_string = ""
    for hold in portions[1].split(", "):
        #print(hold)
        num = re.findall("[\d]*", hold)[0]
        hold_color = re.findall("(?<=\s).+?(?=\sbags*)", hold)[0]
        hold_string = hold_string + str(num) + "," + hold_color + ","
    colors[color] = hold_string

query = "shiny gold"
total_bags = 0
for color in colors.keys():
    if color == query:
        pass
    else:
        hold_string = colors[color]
        if "other" in hold_string:
            pass
        else:
            if find(query, hold_string, colors):
                total_bags += 1

print(total_bags)
