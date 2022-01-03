import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_09.txt") as file:
    input = [line.splitlines()[0] for line in file.readlines()]

input = [list(line) for line in input]
heightmap = np.array(input).astype(int)
heightmap_zeros = np.zeros(heightmap.shape)

def check_right(row, col, height):
    return height < heightmap[row][col+1]
def check_left(row, col, height):
    return height < heightmap[row][col-1]
def check_up(row, col, height):
    return height < heightmap[row-1][col]
def check_down(row, col, height):
    return height < heightmap[row+1][col]

sum_val = 0
rows, columns = heightmap.shape
for row in range(rows):
    for col in range(columns):
        height = heightmap[row][col]
        checker_list = []
        if row > 0:
            checker_list.append(check_up(row, col, height))
        if row < rows-1:
            checker_list.append(check_down(row, col, height))
        if col > 0:
            checker_list.append(check_left(row, col, height))
        if col < columns-1:
            checker_list.append(check_right(row, col, height))
        if all(checker_list):
            sum_val += heightmap[row][col] +1
            heightmap_zeros[row][col] = 1

print("Part 1: " + str(sum_val))

# Part 2
def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
pad_heightmap = np.pad(heightmap, 1, pad_with,padder = 9)
pad_heightmap_zeros = np.pad(heightmap_zeros, 1, pad_with,padder = 0)
low_points = np.where(pad_heightmap_zeros == 1)

def spreader(row,col):
    value = pad_heightmap[row][col]
    if value == 9:
        return 0
    else:
        pad_heightmap[row][col] = 9
        return spreader(row, col+1) + spreader(row, col-1) + spreader(row-1, col) + spreader(row+1, col) + 1

puntos = []
for row,col in zip(low_points[0], low_points[1]):
    puntos.append(spreader(row,col))

puntos_sorted = sorted(puntos)
print("Part 2: " + str(puntos_sorted[-1]* puntos_sorted[-2]* puntos_sorted[-3]))