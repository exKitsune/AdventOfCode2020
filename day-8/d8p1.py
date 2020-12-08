import re
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

accumulator = 0
current_instruction = 0
visited_instructions = { }

while True:
    visited_instructions[current_instruction] = True
    line = input_file[current_instruction]
    instruction, value = line.split(" ")
    mod = value[0]
    num = value[1:]

    if instruction == "acc":
        if mod == "+":
            accumulator += int(num)
        elif mod == "-":
            accumulator -= int(num)
        current_instruction += 1
    
    elif instruction == "nop":
        current_instruction += 1
    elif instruction == "jmp":
        if mod == "+":
            current_instruction += int(num)
        elif mod == "-":
            current_instruction -= int(num)

    if current_instruction in visited_instructions:
        break
    
print(accumulator)