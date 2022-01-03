import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_03.txt") as file:
    report = [line.strip() for line in file.readlines()]

gamma_list = [] #most common
epsilon_list = [] #least common

ones = [0] * len(report[0])
zeros = [0] * len(report[0])
total = [len(report)]* len(report[0])
for line in report:
    i = 0
    for number in line:
        number = int(number)
        if number == 1:
            ones[i] += 1
        i += 1

zeros = np.subtract(total,ones)
for number in range(len(ones)):
    if(ones[number] > zeros[number]):
        gamma_list.append(1)
    else:
        gamma_list.append(0)
    if(ones[number] < zeros[number]):
        epsilon_list.append(1)
    else:
        epsilon_list.append(0)

gamma_dec = ''.join([str(n) for n in gamma_list])
epsilon_dec = ''.join([str(n) for n in epsilon_list])

gamma_bin = int(gamma_dec, 2)
epsilon_bin = int(epsilon_dec, 2)

power_consumption = gamma_bin * epsilon_bin
print("Part 1: " + str(power_consumption))

# Part 2
sum_ones = 0
report_mod = report
j = 0
kept_report_final = None
while True:
    kept_report = []
    sum_zeros = 0
    sum_ones = 0
    for i in range(len(report_mod)):
        number = report_mod[i][j]
        if number == "1":
            sum_ones += 1
    sum_zeros = len(report_mod) - sum_ones

    if sum_ones > sum_zeros:
        for k in range(len(report_mod)):
            if report_mod[k][j] == "1":
                kept_report.append(report_mod[k])
    elif sum_ones < sum_zeros:
        for k in range(len(report_mod)):
            if report_mod[k][j] == "0":
                kept_report.append(report_mod[k])
    elif sum_zeros == sum_ones:
        for k in range(len(report_mod)):
            if report_mod[k][j] == "1":
                kept_report.append(report_mod[k])
    if len(kept_report) == 1:
        kept_report_final = kept_report
        break
    report_mod = kept_report
    j += 1

oxygen_list = kept_report_final
oxygen_dec = ''.join([str(n) for n in oxygen_list])
oxygen_bin = int(oxygen_dec, 2)

sum_ones = 0
report_mod = report
j = 0
kept_report_final = None
while True:
    kept_report = []
    sum_zeros = 0
    sum_ones = 0
    for i in range(len(report_mod)):
        number = report_mod[i][j]
        if number == "1":
            sum_ones += 1
    sum_zeros = len(report_mod) - sum_ones

    if sum_zeros < sum_ones:
        for k in range(len(report_mod)):
            if report_mod[k][j] == "0":
                kept_report.append(report_mod[k])
    elif sum_zeros > sum_ones:
        for k in range(len(report_mod)):
            if report_mod[k][j] == "1":
                kept_report.append(report_mod[k])
    elif sum_zeros == sum_ones:
        for k in range(len(report_mod)):
            if report_mod[k][j] == "0":
                kept_report.append(report_mod[k])
    if len(kept_report) == 1:
        kept_report_final = kept_report
        break
    report_mod = kept_report
    j += 1

co2_list = kept_report_final
co2_dec = ''.join([str(n) for n in co2_list])
co2_bin = int(co2_dec, 2)

print("Part 2: " + str(oxygen_bin * co2_bin))