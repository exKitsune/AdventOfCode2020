with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

import re
import struct
import math

mask = ""
(mem, val) = (0, 0)
ram = dict()

#bits_36 = 0b111111111111111111111111111111111111
set_1 = 0b000000000000000000000000000000000001

def flipX(addr):
    addresses = []
    bit = addr.find('X')

    if bit != -1:
        temp = list(addr)
        temp[bit] = '1'
        addr = "".join(temp)
        addresses += flipX(addr)
        temp = list(addr)
        temp[bit] = '0'
        addr = "".join(temp)
        addresses += flipX(addr)
    else:
        addresses.append(addr)
    return addresses

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
                new_val += 'X'
            else:
                if n == '1' or str((mem >> len(mask) - i - 1) & set_1) == '1':
                    new_val += '1'
                else:
                    new_val += '0'
        
        for addr in flipX(new_val):
            ram[addr] = val
        
sum = 0
for addr in ram:
    sum += ram[addr]

print(sum)
