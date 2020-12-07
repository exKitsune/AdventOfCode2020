import re
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

def find(hold_string, colors):
    nums = hold_string.split(",")[:-1:2]
    holds = hold_string.split(",")[1::2]

    if "other" in holds:
        return 0
    else:
        total = 0
        #print(holds)
        for i in range(0, len(nums)):
            total += int(nums[i]) * find(colors[holds[i]], colors) + int(nums[i])
        #print(hold_string, total)
        return total

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

print(find(colors[query], colors))


