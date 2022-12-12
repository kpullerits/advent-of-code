import os
import numpy as np
from collections import defaultdict
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_09.txt") as file:
    motions = [line.strip().split(" ") for line in file.readlines()]

# h_pos = np.zeros(2)
# t_pos = np.zeros(2)

# t_visited = defaultdict()

# def move_diag(distance_h_t_abs, distance_h_t):
#     diag = np.where(distance_h_t_abs == 1)
#     t_pos[diag] += distance_h_t[diag]

# for i, motion in enumerate(motions):
#     direction = motion[0]
#     steps = int(motion[1])
#     for step in range(steps):
#         if direction == "R":
#             h_pos[1] += 1

#             distance_h_t = h_pos - t_pos
#             distance_h_t_abs = abs(h_pos - t_pos)
#             if 2 in distance_h_t_abs:
#                 if 1 in distance_h_t_abs:
#                     move_diag(distance_h_t_abs, distance_h_t)
#                 t_pos[1] += 1
#         elif direction == "U":
#             h_pos[0] += 1

#             distance_h_t = h_pos - t_pos
#             distance_h_t_abs = abs(h_pos - t_pos)
#             if 2 in distance_h_t_abs:
#                 if 1 in distance_h_t_abs:
#                     move_diag(distance_h_t_abs, distance_h_t)
                
#                 t_pos[0] += 1
#         elif direction == "L":
#             h_pos[1] += -1

#             distance_h_t = h_pos - t_pos
#             distance_h_t_abs = abs(h_pos - t_pos)
#             if 2 in distance_h_t_abs:
#                 if 1 in distance_h_t_abs:
#                     move_diag(distance_h_t_abs, distance_h_t)
                
#                 t_pos[1] += -1
#         elif direction == "D":
#             h_pos[0] += -1

#             distance_h_t = h_pos - t_pos
#             distance_h_t_abs = abs(h_pos - t_pos)
#             if 2 in distance_h_t_abs:
#                 if 1 in distance_h_t_abs:
#                     move_diag(distance_h_t_abs, distance_h_t)
                
#                 t_pos[0] += -1
#         name = str(int(t_pos[0])) + "_" + str(int(t_pos[1]))
#         t_visited[name] = 1

# print("Part 1: " + str(len(t_visited)))

# Part 1 cleaned
knots = 10
h_pos = np.zeros(2)
t_pos = np.zeros(2)
positions = [np.zeros(2) for _ in range(knots)]
t_visited = defaultdict()

for motion in motions:
    direction = motion[0]
    steps = int(motion[1])
    for step in range(steps):
        if direction == "R":
            h_pos[1] += 1
        elif direction == "U":
            h_pos[0] += 1
        elif direction == "L":
            h_pos[1] -= 1
        elif direction == "D":
            h_pos[0] -= 1

        distance_h_t = h_pos - t_pos
        distance_h_t_abs = abs(distance_h_t)
        if 2 in distance_h_t_abs:
            if 1 in distance_h_t_abs:
                index = np.where(abs(distance_h_t) == 1)
                t_pos[index] += distance_h_t[index]
            index = np.where(abs(distance_h_t) == 2)
            t_pos[index] += np.sign(distance_h_t[index])

        name = f"{t_pos[0]},{t_pos[1]}"
        t_visited[name] = 1

print("Part 1: " + str(len(t_visited)))


# Part 2

knots = 10
positions = [np.zeros(2) for _ in range(knots)]
t_visited = defaultdict()

for motion in motions:
    direction = motion[0]
    steps = int(motion[1])
    for step in range(steps):
        if direction == "R":
            positions[0][1] += 1
        elif direction == "U":
            positions[0][0] += 1
        elif direction == "L":
            positions[0][1] -= 1
        elif direction == "D":
            positions[0][0] -= 1

        for i in range(knots - 1):
            distance_h_t = positions[i] - positions[i+1]
            distance_h_t_abs = abs(distance_h_t)
            if 2 in distance_h_t_abs:
                if 1 in distance_h_t_abs:
                    index = np.where(abs(distance_h_t) == 1)
                    positions[i+1][index] += distance_h_t[index]
                index = np.where(abs(distance_h_t) == 2)
                positions[i+1][index] += np.sign(distance_h_t[index])
            if i + 1 == knots - 1:
                name = f"{positions[i+1][0]},{positions[i+1][1]}"
                t_visited[name] = 1

print("Part 2: " + str(len(t_visited)))