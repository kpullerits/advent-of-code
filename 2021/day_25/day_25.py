import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(cur_dir + "\\input_25.txt") as file:
    input = [[char for char in line.rstrip()] for line in file.readlines()]

grid = np.array(input)
rows = len(grid)
cols = len(grid[0])
moved = True
counter = 0
while moved:
    grid_shadow = grid.copy()
    moved = False
    for row in range(rows):
        for col in range(cols):
            if grid_shadow[row, col] == ">":
                if col != cols-1:
                    if grid_shadow[row, col + 1] == ".":
                        grid[row,col+1] = ">"
                        grid[row,col] = "."
                        moved = True
                        
                else:
                    if grid_shadow[row, 0] == ".":
                        grid[row,0] = ">"
                        grid[row,col] = "." 
                        moved = True
                 
    grid_shadow = grid.copy() 
    for row in range(rows):
        for col in range(cols):
            if grid_shadow[row,col] == "v":
                if row != rows - 1:
                    if grid_shadow[row + 1, col] == ".":
                        grid[row + 1, col] = "v"
                        grid[row,col] = "."
                        moved = True
                else:
                    if grid_shadow[0, col] == ".":
                        grid[0, col] = "v"
                        grid[row,col] = "."   
                        moved = True
    counter +=1
    
print("Part 1: " + str(counter))