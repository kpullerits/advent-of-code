import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_08.txt") as file:
    trees = [line.strip() for line in file.readlines()]

trees = [list(line) for line in trees]
trees = np.array(trees).astype(int)

sum_val = 0
rows, columns = trees.shape
for row in range(rows):
    for col in range(columns):
        height = trees[row][col]
        if row in [0, rows-1]:
            sum_val +=1
        elif col in [0, columns-1]:
            sum_val += 1
        else:
            is_visible = False
            #check left
            left = []
            for col2 in range(0,col):
                height2 = trees[row][col2]
                if height2 < height:
                    left.append(True)
                else:
                    left.append(False)
            if all(left):
                sum_val +=1
                continue
            #check right
            right = []
            for col2 in range(col+1,columns):
                height2 = trees[row][col2]
                if height2 < height:
                    right.append(True)
                else:
                    right.append(False)
            if all(right):
                sum_val +=1
                continue
            #check up
            up = []
            for row2 in range(0,row):
                height2 = trees[row2][col]
                if height2 < height:
                    up.append(True)
                else:
                    up.append(False)
            if all(up):
                sum_val +=1
                continue
            #check down
            down = []
            for row2 in range(row+1,rows):
                height2 = trees[row2][col]
                if height2 < height:
                    down.append(True)
                else:
                    down.append(False)
            if all(down):
                sum_val +=1
                continue

print("Part 1: " + str(sum_val))

# Part 2

top_score = 0
rows, columns = trees.shape
for row in range(rows):
    for col in range(columns):
        height = trees[row][col]
        #assumed that the edges will not have the top score
        if row in [0, rows-1]:
            pass
        elif col in [0, columns-1]:
            pass
        else: 
            is_visible = False
            #check left
            left = 0
            for col2 in range(col-1, 0-1, -1):
                height2 = trees[row][col2]
                if height2 < height:
                    left += 1
                else:
                    left += 1
                    break
            #check right
            right = 0
            for col2 in range(col+1,columns):
                height2 = trees[row][col2]
                if height2 < height:
                    right += 1
                else:
                    right += 1
                    break
            #check up
            up = 0
            for row2 in range(row-1, 0-1, -1):
                height2 = trees[row2][col]
                if height2 < height:
                    up += 1
                else:
                    up += 1
                    break
            #check down
            down = 0
            for row2 in range(row+1,rows):
                height2 = trees[row2][col]
                if height2 < height:
                    down += 1
                else:
                    down += 1
                    break
            scenic_score = left * right * up * down
            if scenic_score > top_score:
                top_score = scenic_score

print("Part 2: " + str(top_score))
