import os
import numpy as np
from collections import defaultdict
from collections import Counter
import math
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_11.txt") as file:
    monkey_notes = [line.strip() for line in file.readlines()]

monkey_notes_edit = []
monkey_nr = 0
curr_monkey_notes = []
for i, note in enumerate(monkey_notes):

    if "Monkey" in note:
        note = int(note.replace("Monkey ", "").replace(":", ""))
    elif "Starting items" in note:
        note = note.replace("Starting items: ", "").split(", ")
    elif "Operation" in note:
        note = note.replace("Operation: new = ", "")
    elif "Test:" in note:
        note = int(note.replace("Test: divisible by ", ""))
    elif "If true: " in note:
        note = int(note.replace("If true: throw to monkey ", ""))
    elif "If false: " in note:
        note = int(note.replace("If false: throw to monkey ", ""))

    if note == "" :
        pass
    else:
        curr_monkey_notes.append(note)

    if note == "" or i == len(monkey_notes) - 1:
        monkey_notes_edit.append(curr_monkey_notes)
        curr_monkey_notes = []

inspections_per_monkey = [0 for _ in range(len(monkey_notes_edit))]
round = 0
while True:
    for monkey_index, curr_monkey_notes in enumerate(monkey_notes_edit):
        items = curr_monkey_notes[1].copy()
        operation_raw = curr_monkey_notes[2]
        operation_raw_split = operation_raw.split(" ")
        operator = operation_raw[4]
        old_2x = Counter(operation_raw_split)["old"] == 2
        divisible_by = curr_monkey_notes[3]

        worry_level = None
        for item_index, item in enumerate(items):
            worry_level = int(item)

            if old_2x:
                if operator == "+":
                    worry_level = worry_level + worry_level
                elif operator == "-":
                    worry_level = worry_level - worry_level
                elif operator == "*":
                    worry_level = worry_level * worry_level
                elif operator == "/":
                    worry_level = worry_level / worry_level
            else:
                last_number = int(operation_raw_split[-1])
                if operator == "+":
                    worry_level = worry_level + last_number
                elif operator == "-":
                    worry_level = worry_level - last_number
                elif operator == "*":
                    worry_level = worry_level * last_number
                elif operator == "/":
                    worry_level = worry_level / last_number

            worry_level = int(worry_level / 3)
            if worry_level % divisible_by == 0:
                throw_to = curr_monkey_notes[4] 
                monkey_notes_edit[throw_to][1].append(worry_level)
                monkey_notes_edit[monkey_index][1].remove(item)
            else:
                throw_to = curr_monkey_notes[5]
                monkey_notes_edit[throw_to][1].append(worry_level)
                monkey_notes_edit[monkey_index][1].remove(item)
            inspections_per_monkey[monkey_index] += 1
    round += 1
    if round == 20:
        print(inspections_per_monkey)
        break

inspections_per_monkey.sort(reverse = True)
print("Part 1: " + str(inspections_per_monkey[0] * inspections_per_monkey[1]))

# Part 2

with open(cur_dir + "\\input_11.txt") as file:
    monkey_notes = [line.strip() for line in file.readlines()]

monkey_notes_edit = []
monkey_nr = 0
curr_monkey_notes = []
for i, note in enumerate(monkey_notes):

    if "Monkey" in note:
        note = int(note.replace("Monkey ", "").replace(":", ""))
    elif "Starting items" in note:
        note = note.replace("Starting items: ", "").split(", ")
    elif "Operation" in note:
        note = note.replace("Operation: new = ", "")
    elif "Test:" in note:
        note = int(note.replace("Test: divisible by ", ""))
    elif "If true: " in note:
        note = int(note.replace("If true: throw to monkey ", ""))
    elif "If false: " in note:
        note = int(note.replace("If false: throw to monkey ", ""))

    if note == "" :
        pass
    else:
        curr_monkey_notes.append(note)

    if note == "" or i == len(monkey_notes) - 1:
        monkey_notes_edit.append(curr_monkey_notes)
        curr_monkey_notes = []

inspections_per_monkey = [0 for _ in range(len(monkey_notes_edit))]
round = 0
while True:
    for monkey_index, curr_monkey_notes in enumerate(monkey_notes_edit):
        # items = curr_monkey_notes[1]
        items = curr_monkey_notes[1].copy()
        operation_raw = curr_monkey_notes[2]
        operation_raw_split = operation_raw.split(" ")
        operator = operation_raw[4]
        old_2x = Counter(operation_raw_split)["old"] == 2
        divisible_by = curr_monkey_notes[3]

        worry_level = None
        for item_index, item in enumerate(items):
            worry_level = int(item)

            if old_2x:
                if operator == "+":
                    worry_level = worry_level + worry_level
                elif operator == "-":
                    worry_level = worry_level - worry_level
                elif operator == "*":
                    worry_level = worry_level * worry_level
                elif operator == "/":
                    worry_level = worry_level / worry_level
            else:
                last_number = int(operation_raw_split[-1])
                if operator == "+":
                    worry_level = worry_level + last_number
                elif operator == "-":
                    worry_level = worry_level - last_number
                elif operator == "*":
                    worry_level = worry_level * last_number
                elif operator == "/":
                    worry_level = worry_level / last_number

            worry_level = worry_level % (17 * 19 * 7 * 11 * 13 * 3 * 5 * 2)
            if worry_level % divisible_by == 0:
                throw_to = curr_monkey_notes[4] 
                monkey_notes_edit[throw_to][1].append(worry_level)
                monkey_notes_edit[monkey_index][1].remove(item)
            else:
                throw_to = curr_monkey_notes[5]
                monkey_notes_edit[throw_to][1].append(worry_level)
                monkey_notes_edit[monkey_index][1].remove(item)
            inspections_per_monkey[monkey_index] += 1
    round += 1
    if round == 10000:
        print(inspections_per_monkey)
        break
inspections_per_monkey.sort(reverse = True)

print("Part 2: " + str(inspections_per_monkey[0] * inspections_per_monkey[1]))

