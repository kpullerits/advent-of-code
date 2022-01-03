import os
import numpy as np
from queue import PriorityQueue
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_15.txt") as file:
    input = [line.splitlines()[0] for line in file.readlines()]

input = [list(line) for line in input]
risk_lvl_grid = np.array(input).astype(int)

rows = len(risk_lvl_grid)
cols = len(risk_lvl_grid[0])
start = (0,0)
goal = (rows-1, cols-1)
frontier = PriorityQueue()
frontier.put(start, 0)
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0

def get_neighbours(row, col):
    # Gets coordinates for all neighbours
    n = []
    if row > 0:
        n += [(row-1, col)]
    if row < rows - 1:
        n += [(row+1, col)]
    if col > 0:
        n += [(row, col-1)]
    if col < cols - 1:
        n += [(row, col+1)]
    return n

def cost(row, col):
    return risk_lvl_grid[row, col]

while not frontier.empty():
   current = frontier.get()

   if current == goal:
      break
   
   for next in get_neighbours(current[0], current[1]):
      new_cost = cost_so_far[current] + cost(next[0], next[1])
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost
         frontier.put(next, priority)
         came_from[next] = current

print('Part 1:', cost_so_far[goal])

# Part 2
risk_lvl_grid_big = np.zeros((rows*5, cols*5)) 
for i in range(5):
    for j in range(5):
        risk_lvl_grid_big[i*rows:(i+1)*rows, j*cols: (j+1)*cols] = risk_lvl_grid + i + j 

risk_lvl_grid_big[risk_lvl_grid_big>=10] -=9

rows = len(risk_lvl_grid_big)
cols = len(risk_lvl_grid_big[0])
start = (0,0)
goal = (rows-1, cols-1)
frontier = PriorityQueue()
frontier.put(start, 0)
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0

def cost_big(row, col):
    return risk_lvl_grid_big[row, col]

while not frontier.empty():
   current = frontier.get()

   if current == goal:
      break
   
   for next in get_neighbours(current[0], current[1]):
      new_cost = cost_so_far[current] + cost_big(next[0], next[1])
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost
         frontier.put(next, priority)
         came_from[next] = current
print("Part 2: " + str(cost_so_far[goal]))
