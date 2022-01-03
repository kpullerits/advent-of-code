import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_11.txt") as file:
    input = [line.splitlines()[0] for line in file.readlines()]

input = [list(line) for line in input]
octupus_lvls = np.array(input).astype(int)
has_flashed = np.zeros(octupus_lvls.shape)

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
octupus_lvls = np.pad(octupus_lvls, 1, pad_with,padder = -1)
has_flashed = np.pad(has_flashed, 1, pad_with,padder = -1)

def get_neighbours(row, col):
    l = []
    l.append((row, col+1))
    l.append((row, col-1))
    l.append((row-1, col))
    l.append((row+1, col))
    l.append((row-1, col-1))
    l.append((row-1, col+1))
    l.append((row+1, col-1))
    l.append((row+1, col+1))
    return l

def flasher(row,col):
    if has_flashed[row][col] == 1 or octupus_lvls[row][col] == -1:
        return None
    value = octupus_lvls[row][col]
    if value > 9: # this (row, col) flashes
        has_flashed[row][col] = 1
        n = get_neighbours(row, col)
        for r, c in n:
            if octupus_lvls[r, c] == -1:
                continue
            octupus_lvls[r, c] += 1
            if octupus_lvls[r, c] > 9 and has_flashed[r, c] == 0:
                flasher(r, c)
            

def flasher1(row,col):
    if has_flashed[row][col] == 1 or octupus_lvls[row][col] == -1:
        return None
    octupus_lvls[row][col] = octupus_lvls[row][col] + 1
    value = octupus_lvls[row][col]
    if value > 9: # this (row, col) flashes
        has_flashed[row][col] = 1
        
        flasher1(row, col+1) #right
        flasher1(row, col-1) #left
        flasher1(row-1, col) #up
        flasher1(row+1, col) #down

        flasher1(row-1, col-1) #left up
        flasher1(row-1, col+1) #right up
        flasher1(row+1, col-1) #left down
        flasher1(row+1, col+1) #right down
    return None

rows = octupus_lvls.shape[0]-1
cols = octupus_lvls.shape[1]-1
max_step = 100
sum_flash = 0
for step in range(1,max_step+1,1):
    has_flashed = np.zeros_like(octupus_lvls)
    has_flashed = np.pad(has_flashed, 1, pad_with,padder = -1)
    octupus_lvls[1:rows, 1:cols] = octupus_lvls[1:rows, 1:cols] + 1
    for row in range(1,octupus_lvls.shape[0],1):
        for col in range(1,octupus_lvls.shape[1],1):
            if octupus_lvls[row][col] > 9:
                flasher1(row, col)
    octupus_lvls[octupus_lvls>9] = 0
    sum_flash = sum_flash + len(has_flashed[has_flashed == 1])
print("Part 1 " + str(sum_flash))

# Part 2
with open(cur_dir + "\\input_11.txt") as file:
    input = [line.splitlines()[0] for line in file.readlines()]

input = [list(line) for line in input]
octupus_lvls = np.array(input).astype(int)
has_flashed = np.zeros(octupus_lvls.shape)
octupus_lvls = np.pad(octupus_lvls, 1, pad_with,padder = -1)
has_flashed = np.pad(has_flashed, 1, pad_with,padder = -1)

rows = octupus_lvls.shape[0]-1
cols = octupus_lvls.shape[1]-1

sum_flash = 0
step = 1
while True:
    has_flashed = np.zeros_like(octupus_lvls)
    has_flashed = np.pad(has_flashed, 1, pad_with,padder = -1)
    octupus_lvls[1:rows, 1:cols] = octupus_lvls[1:rows, 1:cols] + 1
    for row in range(1,octupus_lvls.shape[0],1):
        for col in range(1,octupus_lvls.shape[1],1):
            if octupus_lvls[row][col] > 9:
                flasher(row, col)
    octupus_lvls[octupus_lvls>9] = 0
    if step <= 100:
        sum_flash = sum_flash + len(has_flashed[has_flashed == 1])
    if np.all((has_flashed[1:rows, 1:cols]==1)):
        print("Part 2: " + str(step))
        break
    step += 1

print("Part 1 (using part 2 code): " + str(sum_flash))