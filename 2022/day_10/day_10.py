import os
import numpy as np
from collections import defaultdict
import math
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_10.txt") as file:
    instructions = [line.strip().split(" ") for line in file.readlines()]

x = 1
cycle = 1
register = []
interval = [20 + i * 40 for i in range(6)]

def update_register():
    if cycle in interval:
            register.append(cycle * x)

for instruction in instructions:
    if instruction[0] == "noop":
        update_register()
        cycle += 1
    elif instruction[0] == "addx":
        value = int(instruction[1])
        for i in range(2):
            update_register()
            if i == 1:
                x += value
            cycle += 1

print("Part 1: " + str(sum(register)))

# Part 2
crt =[[None for _ in range(40)] for _ in range(6)]

x = 1
cycle = 1

def update_crt():
    sprite_pos = [x-1, x, x + 1]
    pixel = " "
    row_index = math.floor((cycle - 1) / 40)
    col_index = (cycle - 1) % 40
    if col_index in sprite_pos:
        pixel = "#"
    crt[row_index][col_index] = pixel

for instruction in instructions:
    if instruction[0] == "noop":
        update_crt()
        cycle += 1
    elif instruction[0] == "addx":
        value = int(instruction[1])
        for i in range(2):
            update_crt()
            if i == 1:
                x += value
            cycle += 1

print("Part 2: " )
for row in crt:
    print("".join(row))