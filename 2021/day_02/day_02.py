import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_02.txt") as file:
    instructions = [line.strip() for line in file.readlines()]

horizontal = 0
depth = 0

for instruction in instructions:
    forward_or_down =  instruction.split(" ")[0]
    number = int(instruction.split(" ")[1])
    if forward_or_down == "forward":
        horizontal += number
    if forward_or_down == "down":
        depth += number
    elif forward_or_down == "up":
        depth -= number

print("Part 1: " + str(horizontal * depth))

# Part 2
horizontal = 0
depth = 0
aim = 0
for instruction in instructions:
    forward_or_down =  instruction.split(" ")[0]
    number = int(instruction.split(" ")[1])
    if forward_or_down == "forward":
        horizontal += number
        depth = depth + (aim * number)
    if forward_or_down == "down":
        aim += number
    elif forward_or_down == "up":
        aim -= number

print("Part 2: " + str(horizontal * depth))