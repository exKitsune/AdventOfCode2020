from collections import deque
from functools import reduce
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

bus_times = input_file[1].split(',')

currentTime = 0
list_nums = []
for t in bus_times:
    try:
        list_nums.append(int(t))
    except:
        pass

rems = []
mods = []

for i in range(0, len(list_nums)):
    rems.append((list_nums[i] - bus_times.index(str(list_nums[i]))))
    mods.append(list_nums[i])

print(int(chinese_remainder(mods, rems)))
