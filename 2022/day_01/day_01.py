import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_01.txt") as file:
    measurements = [line.strip() for line in file.readlines()]

calories = 0
top_calories = 0
all_elves_cal = []
for i in range(len(measurements)):
    curr_food = measurements[i]
    if curr_food == "":
        all_elves_cal.append(calories)
        calories = 0
    else:
        calories += int(curr_food)
        if calories > top_calories:
            top_calories = calories
print("Part 1: " + str(top_calories))

# Part 2
all_elves_cal.sort(reverse = True)
sum_top_3 = sum(all_elves_cal[0:3])
print("Part 2: " + str(sum_top_3))

