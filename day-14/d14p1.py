with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

import re
import struct

mask = ""
(mem, val) = (0, 0)
ram = dict()

#bits_36 = 0b111111111111111111111111111111111111
set_1 = 0b000000000000000000000000000000000001

for line in input_file:
    if line.startswith("mask = "):
        mask = line.split("= ")[1]
    else:
        m = re.search(r'mem\[(\d+)] = (\d+)', line)
        mem = int(m.group(1))
        val = int(m.group(2))
        new_val = ""

        for i in range(len(mask)):
            n = mask[i]
            if n == 'X':
                new_val += str((val >> len(mask) - i - 1) & set_1)
            elif n == '1':
                new_val += "1"
            elif n == '0':
                new_val += "0"
        #print(new_val)
        new_val = int(new_val, base=2)
        #print(bin(new_val))

        ram[mem] = new_val

sum = 0
for addr in ram:
    sum += ram[addr]

print(sum)