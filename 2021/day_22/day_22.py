import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(cur_dir + "\\input_22.txt") as file:
    input = [line.rstrip().split(" ") for line in file.readlines()]

input2 = [[line[0] ,line[1].split(",")] for line in input]

input3 = []
for line in input2:
    curr_list = []
    if line[0] == "on":
        curr_list.append(1)
    else:
        curr_list.append(0)
    xyz = line[1]
    curr_list.append([int(n)+50 for n in xyz[0][2:].split("..")])
    curr_list.append([int(n)+50 for n in xyz[1][2:].split("..")])
    curr_list.append([int(n)+50 for n in xyz[2][2:].split("..")])
    input3.append(curr_list)
    
    
cuboid = np.zeros((101, 101, 101))

for i, line in enumerate(input3):
    on_off = line[0]
    xmin, xmax = line[1]
    ymin, ymax = line[2] 
    zmin, zmax = line[3] 
    if xmin < 0 or xmax > 100:
        continue
    elif ymin < 0 or ymax > 100:
        continue
    elif zmin < 0 or zmax > 100:
        continue
    else:
        cuboid[xmin:xmax+1,ymin:ymax+1,zmin:zmax+1] = on_off

print("Part 1: " + str(len(cuboid[cuboid>0])))