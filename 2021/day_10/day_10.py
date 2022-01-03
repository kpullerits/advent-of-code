import os
import statistics
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_10.txt") as file:
    input = [line.splitlines() for line in file.readlines()]
    input = [line[0] for line in input]
    
symbol_dict = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}
symbol_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
line_clear = False
first_illegal_char_sum = 0
corrupted_lines = []
incomplete_lines_full = []
incomplete_lines = []
for i, line in enumerate(input):
    line_clear = False
    while line_clear == False:
        for pos_1,symbol in enumerate(line):
            not_found_pair = True
            if symbol in [")", "]", "}", ">"]:
                found_pair = False
                symbol_to_find = symbol_dict[symbol]
                pos_2 = pos_1-1
                symbol_2 = line[pos_2]
                if symbol_2 == symbol_to_find:
                    line1 = line[0: pos_2]
                    line2= line[pos_2+1:pos_1]
                    line3 = line[pos_1+1 :]
                    line_removed = line1 + line2 + line3
                    line = line_removed
                    found_pair = True
                    not_found_pair = False                        
                    break
                else:
                    line_clear = True
                    corrupted_lines.append(input[i])
                    first_illegal_char_sum += symbol_points[symbol]
                    break
            if pos_1 == len(line)-1:
                line_clear = True

                incomplete_lines_full.append(input[i])
                incomplete_lines.append(line)

print("Part 1: " + str(first_illegal_char_sum))

# Part 2
incomplete_lines_flipped = []
for line in incomplete_lines:
    incomplete_lines_flipped.append(line[len(line)::-1])

symbol_dict2 = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
incomplete_lines_flipped_change_char = []
for line in incomplete_lines_flipped:
    new_line = ""
    for char in line:
        new_line += symbol_dict2[char]
    incomplete_lines_flipped_change_char.append(new_line)

symbol_points2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
def calc_score(line):
    tot_score = 0
    for char in line:
        tot_score *= 5
        tot_score += symbol_points2[char]
    return tot_score

incomplete_lines_flipped_change_char_scores = []
for line in incomplete_lines_flipped_change_char:
    incomplete_lines_flipped_change_char_scores.append(calc_score(line))

print("Part 2: " + str(statistics.median(incomplete_lines_flipped_change_char_scores)))
