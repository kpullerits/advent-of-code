import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_06.txt") as file:
    datastream = file.read()

first_marker = None
for marker in range(0, len(datastream) - 4):
    four_char = datastream[marker : marker + 4]
    count = 0
    for i, char1 in enumerate(four_char):
        for j, char2 in enumerate(four_char):
            if i == j:
                continue
            if char1 == char2:
                continue
            count += 1

    if count == 12:
        print(str(four_char))
        first_marker = marker + 4
        break

    
print("Part 1: " + str(first_marker))

# Part 2
first_marker = None
for marker in range(0, len(datastream) - 14):
    four_char = datastream[marker : marker + 14]
    count = 0
    for i, char1 in enumerate(four_char):
        for j, char2 in enumerate(four_char):
            if i == j:
                continue
            if char1 == char2:
                continue
            count += 1

    if count == 13*14:
        print(str(four_char))
        first_marker = marker + 14
        break
print("Part 2: " + str(first_marker))

