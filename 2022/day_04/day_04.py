import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_04.txt") as file:
    assignment_pairs = [line.strip().split(",") for line in file.readlines()]

assignment_pairs = [[elf.split("-") for elf in line] for line in assignment_pairs]

def populate_coord(val_range, coord_system):
    for i in val_range:
        coord_system[i] = 1


counter = 0
for pair in assignment_pairs:

    
    pair1_range = range(int(pair[0][0])-1, int(pair[0][1]))
    pair2_range = range(int(pair[1][0])-1, int(pair[1][1]))
    
    max_val = max(int(pair[0][1]), int(pair[1][1]))

    coord1 = np.zeros(max_val)
    coord2 = np.zeros(max_val)

    populate_coord(pair1_range, coord1)
    populate_coord(pair2_range, coord2)

    coord1_zeros = len(coord1[coord1 == 0])
    coord2_zeros = len(coord2[coord2 == 0])

    sum_coord = coord1 + coord2
    sum_coord_zeros = len(sum_coord[sum_coord == 0])
    if sum_coord_zeros == coord1_zeros or sum_coord_zeros == coord2_zeros:
        counter += 1

print("Part 1: " + str(counter))

# Part 2
counter = 0
for pair in assignment_pairs:

    
    pair1_range = range(int(pair[0][0])-1, int(pair[0][1]))
    pair2_range = range(int(pair[1][0])-1, int(pair[1][1]))
    
    max_val = max(int(pair[0][1]), int(pair[1][1]))

    coord1 = np.zeros(max_val)
    coord2 = np.zeros(max_val)

    populate_coord(pair1_range, coord1)
    populate_coord(pair2_range, coord2)

    sum_coord = coord1 + coord2
    sum_coord_zeros = len(sum_coord[sum_coord == 2])
    if sum_coord_zeros > 0:
        counter += 1
print("Part 2: " + str(counter))

