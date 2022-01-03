import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_13_dots.txt") as file:
    input = [line.splitlines() for line in file.readlines()]

input_dots = [line[0].split(",") for line in input]


max_row = 0
max_col = 0
for i, line in enumerate(input_dots):
    for j, number in enumerate(line):
        number_int = int(number)
        input_dots[i][j] = number_int
        if j == 0:
            if number_int > max_col:
                max_col = number_int
        if j == 1:
            if number_int > max_row:
                max_row = number_int

with open(cur_dir + "\\input_13_fold.txt") as file:
    input = [line.splitlines() for line in file.readlines()]
fold_input = [line[0].split("=") for line in input]

paper = np.zeros((max_row+1, max_col+1))

for line in input_dots:
    row = line[1]
    col = line[0]
    paper[row, col] = 1

i = 0
for i, fold in enumerate(fold_input):
    if i > 0:
        break
    up_or_left = fold[0]
    if up_or_left == "fold along y":
        row = int(fold[1])
        paper1 = paper[0:row, :]
        paper2 = paper[row+1:, :]
        
        paper2_flip = np.flipud(paper2)

        new_paper = paper1 + paper2_flip
        visible_dots = len(new_paper[new_paper>=1])
        print("Part 1: " + str(visible_dots))

    elif up_or_left == "fold along x":
        col = int(fold[1])

        paper1 = paper[:, 0:col]
        paper2 = paper[:, col+1:]
        
        paper2_flip = np.fliplr(paper2)

        new_paper = paper1 + paper2_flip
        visible_dots = len(new_paper[new_paper>=1])
        print("Part 1: " + str(visible_dots))



# Part 2
new_paper = paper
for i, fold in enumerate(fold_input):
    paper = new_paper
    up_or_left = fold[0]
    if up_or_left == "fold along y":
        row = int(fold[1])
        paper1 = paper[0:row, :]
        paper2 = paper[row+1:, :]
        
        paper2_flip = np.flipud(paper2)

        new_paper = paper1 + paper2_flip
        visible_dots = len(new_paper[new_paper>=1])

    elif up_or_left == "fold along x":
        col = int(fold[1])

        paper1 = paper[:, 0:col]
        paper2 = paper[:, col+1:]
        
        paper2_flip = np.fliplr(paper2)

        new_paper = paper1 + paper2_flip
        visible_dots = len(new_paper[new_paper>=1])

print("Part 2: ")
for i in range(len(new_paper)):
    s = ''
    for j in range(len(new_paper[0])):
        if new_paper[i,j] > 0:
            s += '#'
        else:
            s += '.'
    print(s)

print("E    C    F    H    L    H    Z    F")