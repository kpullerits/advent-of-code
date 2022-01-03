import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_05.txt") as file:
    input = [line.splitlines() for line in file.readlines()]

input2 = [line[0].split(" -> ") for line in input]

input3 = [None] * len(input2)
for i,line in enumerate(input2):
    pair_new = [None] * len(line)
    for j,pair in enumerate(line):
        pair_new[j] = pair.split(",")
    input3[i] = pair_new

input4 = input3
for i,line in enumerate(input3):
    for j,pair in enumerate(line):
        for y,number in enumerate(pair):
            input4[i][j][y] = int(number)

#what is max x/y?
max_x = 0
max_y = 0

for line in input4:
    for pair in line:
        if pair[0] > max_x:
            max_x = pair[0]
        if pair[1] > max_y:
            max_y = pair[1]

#only keep hor/ver lines
input5 =  []
for line in input4:
    if line[0][0] ==  line[1][0]:
        input5 += [line]
    if line[0][1] ==  line[1][1]:
        input5 += [line]

#construct matrix
line_matrix = np.zeros((max_x+2, max_y+2)) #+2 since it is shift


for line in input5:
    pair1 = line[0]
    pair2 = line[1]
    if pair1[0] == pair2[0]:
        col_coord = pair1[0]
        line_length = abs(pair1[1] - pair2[1])
        min_row_coord = min(pair1[1], pair2[1])
        line_matrix[min_row_coord:min_row_coord+line_length+1, col_coord] += 1
    
    if pair1[1] == pair2[1]:
        row_coord = pair1[1]
        line_length = abs(pair1[0] - pair2[0])
        min_col_coord = min(pair1[0], pair2[0])
        line_matrix[row_coord, min_col_coord:min_col_coord+line_length+1] += 1
    
print("Part 1: " + str(len(line_matrix[line_matrix>1])))

# Part 2

#only keep hor/ver lines as input 5 and diag as input_diag
input5 =  []
input_diag = []
for line in input4:
    if line[0][0] ==  line[1][0]:
        input5 += [line]
    elif line[0][1] ==  line[1][1]:
        input5 += [line]
    else:
        input_diag += [line]


#construct matrix
line_matrix = np.zeros((max_x+2, max_y+2)) #+2 since it is shift

for line in input5:
    pair1 = line[0]
    pair2 = line[1]
    if pair1[0] == pair2[0]:
        col_coord = pair1[0]
        line_length = abs(pair1[1] - pair2[1])
        min_row_coord = min(pair1[1], pair2[1])
        line_matrix[min_row_coord:min_row_coord+line_length+1, col_coord] += 1
    
    if pair1[1] == pair2[1]:
        row_coord = pair1[1]
        line_length = abs(pair1[0] - pair2[0])
        min_col_coord = min(pair1[0], pair2[0])
        line_matrix[row_coord, min_col_coord:min_col_coord+line_length+1] += 1
    

for line in input_diag:
    pair1 = line[0]
    pair2 = line[1]
    if pair1[0] < pair2[0]:
        line_length = abs(pair1[0] - pair2[0]) +1
        if pair1[1] < pair2[1]:
            for i in range(line_length):
                line_matrix[pair1[1]+i, pair1[0]+i] += 1
        else:
            for i in range(line_length):
                line_matrix[pair1[1]-i, pair1[0]+i] += 1
    else:
        line_length = abs(pair1[0] - pair2[0]) +1
        if pair1[1] > pair2[1]:
            for i in range(line_length):
                line_matrix[pair2[1]+i, pair2[0]+i] += 1
        else:
            for i in range(line_length):
                line_matrix[pair2[1]-i, pair2[0]+i] += 1   


print("Part 2: " + str(len(line_matrix[line_matrix>1])))