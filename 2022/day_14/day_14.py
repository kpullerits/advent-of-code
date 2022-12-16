import os
import numpy as np
from queue import Queue
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_14.txt") as file:
    input = [[[int(n) for n in line2.split(",")] for line2 in line.strip().split(" -> ")] for line in file.readlines()]

min_x, max_x = 500, 500
min_y, max_y = 0, 0
for line in input:
    for coord in line:
        x = int(coord[0])
        y = int(coord[1])
        if min_x > x:
            min_x = x
        if max_x < x:
            max_x = x
        if min_y > y:
            min_y = y
        if max_y < y:
            max_y = y
input = [[[pos[0] - min_x, pos[1]] for pos in line] for line in input]

def print_grid(grid):
    print('\n')
    for row in grid:
        s = ''
        for col in row:
            if col == 1:
                s += '#'
            elif col == -1:
                s += 'X'
            elif col == 2:
                s += 'o'
            else:
                s += '.'
        print(s)
max_y2 = (max_y - min_y) + 1 + 1
max_x2 = (max_x - min_x) + 1 + 2
scan_np = np.zeros((max_y2, max_x2)).astype(int)
scan_np[-1, :] = -1
scan_np[:, 0] = -1
scan_np[:, -1] = -1

for line in input:
    for i in range(len(line) - 1):
        x1, y1 = int(line[i][0]) + 1, int(line[i][1])
        x2, y2 = int(line[i + 1][0]) + 1, int(line[i + 1][1]) 
        diff_x = x2 - x1
        diff_y = y2 - y1
        if diff_x == 0:
            if y1 < y2:
                scan_np[y1: y2 + 1, x1] = 1
            else:
                scan_np[y2: y1 + 1, x1] = 1
        else:
            if x1 < x2:
                scan_np[y1, x1: x2 + 1] = 1
            else:
                scan_np[y1, x2: x1 + 1] = 1

def next_pos(grid, x, y):
    is_possible = [0, -1]
    #down
    if grid[y + 1, x] in is_possible:
        return (x, y + 1)
    #down left
    elif grid[y + 1, x - 1] in is_possible:
        return (x - 1, y + 1)
    #down right
    elif grid[y + 1, x + 1] in is_possible:
        return (x + 1, y + 1)
    else:
        return None
counter = 0
brejk = False
while not brejk:
    curr_posit = (500 - min_x + 1, 0)
    while True:
        
        next_posit = next_pos(scan_np, curr_posit[0], curr_posit[1])
        if next_posit is None:
            scan_np[curr_posit[1], curr_posit[0]] = 2
            counter += 1
            break
        elif scan_np[next_posit[1], next_posit[0]] == -1:
            brejk = True
            break
        else:
            curr_posit = next_posit



print("Part 1: " + str(counter))

# Part 2
max_y2 = (max_y - min_y) + 1 + 1 + 1
pad = max_y2*2

max_x2 = (max_x - min_x) + 1 + 2 + pad
scan_np = np.zeros((max_y2, max_x2)).astype(int)
scan_np[-2, :] = 0
scan_np[-1, :] = 1

for line in input:
    for i in range(len(line) - 1):
        x1, y1 = int(line[i][0]) + 1 + int(pad/2), int(line[i][1])
        x2, y2 = int(line[i + 1][0]) + 1 + int(pad/2), int(line[i + 1][1]) 
        diff_x = x2 - x1
        diff_y = y2 - y1
        if diff_x == 0:
            if y1 < y2:
                scan_np[y1: y2 + 1, x1] = 1
            else:
                scan_np[y2: y1 + 1, x1] = 1
        else:
            if x1 < x2:
                scan_np[y1, x1: x2 + 1] = 1
            else:
                scan_np[y1, x2: x1 + 1] = 1

def next_pos(grid, x, y):
    is_possible = [0, -1]
    #down
    if grid[y + 1, x] in is_possible:
        return (x, y + 1)
    #down left
    elif grid[y + 1, x - 1] in is_possible:
        return (x - 1, y + 1)
    #down right
    elif grid[y + 1, x + 1] in is_possible:
        return (x + 1, y + 1)
    else:
        return None

counter = 0
brejk = False
while not brejk:
    curr_posit = (500 - min_x + 1 + int(pad/2), 0)
    while True:
        
        next_posit = next_pos(scan_np, curr_posit[0], curr_posit[1])
        if next_posit is None:
            if scan_np[curr_posit[1], curr_posit[0]] == 2:
                brejk = True
                break
            scan_np[curr_posit[1], curr_posit[0]] = 2
            counter += 1
            break
        else:
            curr_posit = next_posit

print("Part 2: " + str(counter))


