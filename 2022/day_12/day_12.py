import os
import numpy as np
from queue import Queue
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_12.txt") as file:
    heightmap = [line.strip() for line in file.readlines()]

heightmap = [list(line) for line in heightmap]

start_pos = (None, None)
end_pos = (None, None)
for i, row in enumerate(heightmap):
    for j, char in enumerate(row):
        if "S" in char:
            start_pos = (i, j)
        if "E" in char:
            end_pos = (i, j)
n = ord('a')

def get_neighbor(pos):
    neighbors = []
    if pos[1] > 0:
        neighbors.append((pos[0], pos[1] - 1))
    if pos[0] > 0:
        neighbors.append((pos[0] - 1, pos[1]))
    if pos[1] < len(heightmap[0]) - 1:
        neighbors.append((pos[0], pos[1] + 1))
    if pos[0] < len(heightmap) - 1:
        neighbors.append((pos[0] + 1, pos[1]))

    return neighbors

def get_height_value(pos):
    height_char = heightmap[pos[0]][pos[1]]
    if height_char == 'S':
        height_char = 'a'
    elif height_char == 'E':
        height_char = 'z'
    neighbor_nmr = ord(height_char)
    return neighbor_nmr

frontier = Queue()
frontier.put(start_pos)
came_from = dict()
came_from[start_pos] = None

found_goal = False
while not frontier.empty():
    current = frontier.get()

    if current == end_pos: 
        found_goal = True
        break           
    
    neighbor_list = get_neighbor(current)
    curr_nmr = get_height_value(current)
    neighbor_list_ok = []

    for neighbor in neighbor_list:
        neighbor_nmr = get_height_value(neighbor)
        if neighbor_nmr <= curr_nmr + 1:
            neighbor_list_ok.append(neighbor)

    for next in neighbor_list_ok:
        if next not in came_from:
            frontier.put(next)
            came_from[next] = current


if found_goal:
    current_pos_backtrack = end_pos
    counter = 0
    while current_pos_backtrack != start_pos:
        current_pos_backtrack = came_from[current_pos_backtrack]
        counter += 1

    print("Part 1: " + str(counter))

# Part 2
start_pos = []
for i, row in enumerate(heightmap):
    for j, char in enumerate(row):
        if "a" in char:
            start_pos.append((i, j))

overall_count = []
for start in start_pos:
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    came_from[start] = None

    found_goal = False
    while not frontier.empty():
        current = frontier.get()

        if current == end_pos: 
            found_goal = True
            break           
        
        neighbor_list = get_neighbor(current)
        curr_nmr = get_height_value(current)
        neighbor_list_ok = []

        for neighbor in neighbor_list:
            neighbor_nmr = get_height_value(neighbor)
            if neighbor_nmr <= curr_nmr + 1:
                neighbor_list_ok.append(neighbor)

        for next in neighbor_list_ok:
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current


    if found_goal:
        current_pos_backtrack = end_pos
        counter = 0
        while current_pos_backtrack != start:
            current_pos_backtrack = came_from[current_pos_backtrack]
            counter += 1
        overall_count.append(counter)

print("Part 2: " + str(min(overall_count)))


