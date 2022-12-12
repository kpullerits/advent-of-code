import os
import sys
from itertools import repeat
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_07.txt") as file:
    file_browsing = [line.strip() for line in file.readlines()]

print(file_browsing)

file_sizes = {}
subdirs = {}
curr_dir = None
for i in range(len(file_browsing)):
    line = file_browsing[i]
    if line[0] == "$":
        command = line.split(" ")
        if command[1] == "cd":
            if command[2] == "/":
                curr_dir = "\\"
            else:
                curr_dir = os.path.normpath(os.path.join(curr_dir, command[2]))
            if curr_dir not in subdirs:
                subdirs[curr_dir] = []
                file_sizes[curr_dir] = 0
        elif command[1] == "ls":
            while True:

                line_forward = file_browsing[i+1]
                if line_forward[0] == "$":
                    break
                file = line_forward.split(" ")
                if file[0] == "dir": #dir
                    subdirs[curr_dir].append(os.path.normpath(os.path.join(curr_dir, file[1])))
                else: #file
                    file_sizes[curr_dir] += int(file[0])
                i += 1
                if i+1 >= len(file_browsing):
                    break


print(file_sizes)

def dir_size(directory):
    size = file_sizes[directory]
    for subdir in subdirs[directory]:
        size += dir_size(subdir)
    return size
counter = 0
for directory in file_sizes:
    size = dir_size(directory)
    if size <= 100000:
        counter += size
print("Part 1: " + str(counter))
# Part 2

unused_space = 70000000 - dir_size("\\")
size_to_delete = 30000000 - unused_space
dir_to_delete = None
dir_to_delete_size = sys.maxsize
for directory in file_sizes:
    size = dir_size(directory)
    if size >= size_to_delete and size < dir_to_delete_size:
        dir_to_delete = directory
        dir_to_delete_size = size
print("Part 2: " + str(dir_to_delete) + ", size: " + str(dir_to_delete_size))
