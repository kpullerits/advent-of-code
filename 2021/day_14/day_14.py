import os
import numpy as np
from collections import defaultdict
from collections import Counter
cur_dir = os.path.dirname(os.path.abspath(__file__))

#Part 1
with open(cur_dir + "\\input_14.txt") as file:
    input = [line.splitlines() for line in file.readlines()]

pair_insertion = [line[0].split(" -> ") for line in input]

# polymer_template = "NNCB" #test input
polymer_template = "FNFPPNKPPHSOKFFHOFOC" #input

polymer_template_final = polymer_template
steps = 1
while steps <= 10:
    polymer_template_new = ""
    polymer_template_pairs = []
    for i in range(len(polymer_template_final)-1):
        polymer_template_pairs.append(polymer_template_final[i:i+2])
    polymer_template_pairs_match = [False for _ in range(len(polymer_template_final))]

    for i, pair in enumerate(polymer_template_pairs):
        for j, line in enumerate(pair_insertion):
            pair_rule = line[0]
            insert_element = line[1]
            if pair == pair_rule:
                if i > 0:
                    if polymer_template_pairs_match[i-1] == False:
                        polymer_template_new += pair[0] + insert_element + pair[1] 
                        polymer_template_pairs[i] = True
                    elif polymer_template_pairs_match[i-1] == True:
                        polymer_template_new += insert_element + pair[1] 
                        polymer_template_pairs_match[i] = True
                elif i == 0:
                    polymer_template_new += polymer_template_new + pair[0] + insert_element + pair[1] 
                    polymer_template_pairs_match[i] = True
    polymer_template_final = polymer_template_new
    steps += 1

counter_1 = defaultdict(int)
for character in polymer_template_final:
    counter_1[character] += 1

print("Part 1: " + str(max(counter_1.values()) - min(counter_1.values())))

# Part 2

polymer_template_final = polymer_template

polymer_template_pairs = []
for i in range(len(polymer_template)-1):
        polymer_template_pairs.append(polymer_template[i:i+2])

polymer_template_dict = defaultdict(int)
for k in polymer_template_pairs:
    polymer_template_dict[k] += 1

polymer_template_dict_final = polymer_template_dict
steps = 1
while steps <= 40:
    polymer_template_dict_new = defaultdict(int)
    for pair, value in polymer_template_dict_final.items():
        for j, line in enumerate(pair_insertion):
            pair_rule = line[0]
            insert_element = line[1]
            if pair == pair_rule:
                polymer_template_dict_new[pair] -= value
                polymer_template_dict_new[pair[0] + insert_element] += value
                polymer_template_dict_new[insert_element + pair[1]] += value

    a_counter = Counter(polymer_template_dict_final) 
    b_counter = Counter(polymer_template_dict_new)          
    polymer_template_dict_final = a_counter + b_counter
    steps += 1

counter_2 = defaultdict(int)
for pair, n in polymer_template_dict_final.items():
    if n > 0:
        counter_2[pair[0]] += n
        counter_2[pair[1]] += n


counter_2[polymer_template[0]] += 1 
counter_2[polymer_template[-1]] += 1

counter_2_no_duplicate = {}
for key, value in counter_2.items():
    counter_2_no_duplicate[key] = int(value/2)

print("Part 2: " + str(max(counter_2_no_duplicate.values()) - min(counter_2_no_duplicate.values())))