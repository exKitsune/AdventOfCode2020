import re
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

accumulator = 0
current_instruction = 0
visited_instructions = { }

attempted = {}

found = False

while not found:
    accumulator = 0
    this_try = True
    visited_instructions = {}
    current_instruction = 0
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

        
        if instruction == "nop":
            if current_instruction not in attempted and this_try:
                #print(current_instruction)
                attempted[current_instruction] = True
                if mod == "+":
                    current_instruction += int(num)
                elif mod == "-":
                    current_instruction -= int(num)
                
                this_try = False
            else:
                current_instruction += 1
        if instruction == "jmp":
            if current_instruction not in attempted and this_try:
                #print(current_instruction)
                attempted[current_instruction] = True
                current_instruction += 1
                this_try = False
            else:
                if mod == "+":
                    current_instruction += int(num)
                elif mod == "-":
                    current_instruction -= int(num)

        

        if not this_try:
            try:
                test = input_file[current_instruction]
            except:
                found = True
                break

       

        if current_instruction in visited_instructions:
            break
    #print(attempted)
print(accumulator)
