import os
cur_dir = os.path.dirname(os.path.abspath(__file__))
from string import ascii_lowercase
from string import ascii_uppercase

# Part 1
with open(cur_dir + "\\input_03.txt") as file:
    rucksack_info = [line.strip() for line in file.readlines()]

lowercase = {v:k+1 for k,v in enumerate(ascii_lowercase)}
uppercase = {v:k+27 for k,v in enumerate(ascii_uppercase)}
prio_list = {**lowercase, **uppercase}

counter = 0
for rucksack in rucksack_info:
    comp1 = rucksack[slice(0, len(rucksack)//2)]
    comp2 = rucksack[slice(len(rucksack)//2, len(rucksack))]

    common_item = set(comp1).intersection(comp2).pop()

    priority_num = prio_list[common_item]
    counter += priority_num

print("Part 1: " + str(counter))

# Part 2
counter = 0
for i in range(0, len(rucksack_info),3):
    rucksack1 = rucksack_info[i]
    rucksack2 = rucksack_info[i+1]
    rucksack3 = rucksack_info[i+2]

    badge = set("".join(set(rucksack1).intersection(rucksack2))).intersection(rucksack3).pop()
    sticker_attachment = prio_list[badge]
    counter += sticker_attachment
print("Part 2: " + str(counter))

