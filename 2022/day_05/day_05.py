import os
from itertools import repeat
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
# Divide input to input_05-crates.txt (crates) and input_05-rearr.txt (rearrangement)
n_crates = 9
with open(cur_dir + "\\input_05-crates.txt") as file: 
    crates = [line for line in file.readlines()]

crates_stack = d = [[] for i in repeat(None, n_crates)]
for line in crates:
    for position in range(0, n_crates):
        crate = line[(position * 4) + 1  : (position * 4) + 2]
        if crate == " ":
            pass
        else:
            crates_stack[position].append(crate)

creates_stack_sort = []
for crate in crates_stack:
    creates_stack_sort.append(crate[::-1])

with open(cur_dir + "\\input_05-rearr.txt") as file:
    rearrangement_list = [line.strip().replace("move ", "").split(" from ") for line in file.readlines()]

rearrangement_list_edit = []
for line in rearrangement_list:
    rearrangement_list_edit.append([int(line[0]), [int(number) for number in line[1].split(" to ")]])


for rearrangement in rearrangement_list_edit:
    move_n = rearrangement[0]
    from_crate = rearrangement[1][0] - 1
    to_crate = rearrangement[1][1] - 1
    for move in range(move_n):
        to_move = creates_stack_sort[from_crate].pop()
        creates_stack_sort[to_crate].append(to_move)

message = ""
for i in range(n_crates):
    message += creates_stack_sort[i][-1]
print("Part 1: " + str(message))

# Part 2

n_crates = 9
with open(cur_dir + "\\input_05-crates.txt") as file:
    crates = [line for line in file.readlines()]

crates_stack = d = [[] for i in repeat(None, n_crates)]
for line in crates:
    for position in range(0, n_crates):
        crate = line[(position * 4) + 1  : (position * 4) + 2]
        if crate == " ":
            pass
        else:
            crates_stack[position].append(crate)

creates_stack_sort = []
for crate in crates_stack:
    creates_stack_sort.append(crate[::-1])

with open(cur_dir + "\\input_05-rearr.txt") as file:
    rearrangement_list = [line.strip().replace("move ", "").split(" from ") for line in file.readlines()]

rearrangement_list_edit = []
for line in rearrangement_list:
    rearrangement_list_edit.append([int(line[0]), [int(number) for number in line[1].split(" to ")]])


for rearrangement in rearrangement_list_edit:
    move_n = rearrangement[0]
    from_crate = rearrangement[1][0] - 1
    to_crate = rearrangement[1][1] - 1
    if move_n == 1:
        to_move = creates_stack_sort[from_crate].pop()
        creates_stack_sort[to_crate].append(to_move)
    else:
        to_move = creates_stack_sort[from_crate][-move_n:]
        for crate in to_move:
            creates_stack_sort[to_crate].append(crate)
        for _ in range(move_n):
            to_move = creates_stack_sort[from_crate].pop()

message = ""
for i in range(n_crates):
    message += creates_stack_sort[i][-1]

print("Part 2: " + str(message))