import os
import time
from itertools import permutations 
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_08.txt") as file:
    input = [line.splitlines() for line in file.readlines()]

input2 = [line[0].split(" | ") for line in input]

input3 = []
for i in range(len(input2)):
    line_list = []
    line = input2[i]
    for j in range(len(line)):
        chunk = line[j]
        line_list += [chunk.split(" ")]
    input3 += [line_list]

counter = 0
for line in input3:
    for chunk in line[1]:
        if len(chunk) in [2,3,4,7]:
            counter += 1
print("Part 1: " + str(counter))

# Part 2
input4 = []
for line in input3:
    line_list = []
    for j, in_out in enumerate(line):
        in_out_list = []
        for chunk in in_out:
            sorted_chunk = sorted(chunk)
            in_out_list += ["".join(sorted_chunk)]
        line_list += [in_out_list]
    input4 += [line_list]

map_orig = { #original system
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}

permut_list = list(permutations("abcdefg"))
total_sum = 0
for line in input4:
    line_sum = ""
    line_input = line[0]
    line_output = line[1]
    for permut in permut_list:
        map_new = { #new system
            permut[0] : "a",
            permut[1] : "b",
            permut[2] : "c",
            permut[3] : "d",
            permut[4] : "e",
            permut[5] : "f",
            permut[6] : "g"
        }
        line_input_orig = []
        for chunk in line_input:
            chunk_orig = ""
            for letter in chunk:
                chunk_orig += map_new[letter]
            line_input_orig += [chunk_orig]

        line_input_orig = ["".join(sorted(chunk)) for chunk in line_input_orig] #sort
        
        if all(item in list(map_orig.keys()) for item in line_input_orig):
            line_output_orig = []
            for chunk in line_output:
                chunk_orig = ""
                for letter in chunk:
                    chunk_orig += map_new[letter]
                line_output_orig += [chunk_orig]

            line_output_orig = ["".join(sorted(chunk)) for chunk in line_output_orig] #sort

            for chunk in line_output_orig:
                line_sum += str(map_orig[chunk])
            total_sum += int(line_sum)
            break
print("Part 2: " + str(total_sum))