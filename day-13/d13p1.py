from collections import deque
import math
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

wait = int(input_file[0])
bus_ids = list(map(lambda y: int(y),filter(lambda x: x != 'x', input_file[1].split(","))))

bus_waits = []
for id in bus_ids:
    closest_wait = math.ceil(wait / id)
    bus_waits.append(id * closest_wait - wait)

target = min(bus_waits)
idx = bus_waits.index(target)
print(bus_ids[idx] * target)