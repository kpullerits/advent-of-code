import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_01.txt") as file:
    measurements = [int(line.strip()) for line in file.readlines()]

counter = 0
for i in range(len(measurements)):
    curr_measurement = measurements[i]
    if i == 0:
        pass
    else:
        if curr_measurement > measurements[i-1]:
            counter += 1
print("Part 1: " + str(counter))

# Part 2
counter_part2 = 0
measurements_sliding_ave = []
for i in range(len(measurements)-2):
    sum_i = sum(measurements[i:i+3])
    measurements_sliding_ave.append(sum_i)

for i in range(len(measurements_sliding_ave)):
    curr_measurement = measurements_sliding_ave[i]
    if i == 0:
        pass
    else:
        if curr_measurement > measurements_sliding_ave[i-1]:
            counter_part2 += 1
print("Part 2: " + str(counter_part2))