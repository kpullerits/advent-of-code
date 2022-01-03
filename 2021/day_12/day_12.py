import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

#Part 1
with open(cur_dir + "\\input_12.txt") as file:
    input = [line.splitlines() for line in file.readlines()]

input = [line[0].split("-") for line in input]


i = 0
letter_to_number = {}
for line in input:
    for cave in line:
        if cave not in letter_to_number:
            letter_to_number[cave] = i
            i += 1

number_to_letter = inv_map = {v: k for k, v in letter_to_number.items()}

from collections import defaultdict
# graph3 https://www.geeksforgeeks.org/find-paths-given-source-destination/
class Graph3:

    def __init__(self, vertices):
		# No. of vertices
        self.V = vertices
		# default dictionary to store graph
        self.graph = defaultdict(list)
        self.total_sum = 0

	# function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path):

		# Mark the current node as visited and store in path
        if number_to_letter[u].islower():
            visited[u]= True
        path.append(number_to_letter[u])
            
		# If current vertex is same as destination, then print
		# current path[]
        if u == d:
            # print(path)
            self.total_sum += 1
            # print(self.total_sum)
        else:
			# If current vertex is not destination
			# Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i]== False:
                    self.printAllPathsUtil(i, d, visited, path)
					
		# Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False


	# Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

		# Mark all the vertices as not visited
        visited =[False]*(self.V)
        
        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)

number_of_caves = len(letter_to_number)

cave_system = Graph3(number_of_caves)

for line in input:
    cave1 = line[0]
    cave2 = line[1]

    if cave1 == "start":
        cave_system.addEdge(letter_to_number[cave1],letter_to_number[cave2])
    elif cave2 == "start":
        cave_system.addEdge(letter_to_number[cave2],letter_to_number[cave1])
    elif cave1 == "end":
        cave_system.addEdge(letter_to_number[cave2],letter_to_number[cave1])
    elif cave2 == "end":
        cave_system.addEdge(letter_to_number[cave1],letter_to_number[cave2])
    else:
        cave_system.addEdge(letter_to_number[cave1],letter_to_number[cave2])
        cave_system.addEdge(letter_to_number[cave2],letter_to_number[cave1])

cave_system.printAllPaths(letter_to_number["start"], letter_to_number["end"])
print("Part 1: " + str(cave_system.total_sum))

# Part 2

class Graph4:

    def __init__(self, vertices):
		# No. of vertices
        self.V = vertices
		# default dictionary to store graph
        self.graph = defaultdict(list)
        self.total_sum = 0

	# function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path, visited_n, small_caves_twice):

        path.append(number_to_letter[u])
        visited[u] = True
        visited_n[u] = visited_n[u] + 1   
                
		# If current vertex is same as destination, then print
		# current path[]
        if u == d:
            self.total_sum += 1
        else:
			# If current vertex is not destination
			# Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if number_to_letter[i].isupper() or visited_n[i] == 0:
                    self.printAllPathsUtil(i, d, visited, path, visited_n, small_caves_twice)
                elif visited_n[i] == 1 and not small_caves_twice:
                    small_caves_twice = True
                    self.printAllPathsUtil(i, d, visited, path, visited_n, small_caves_twice)
                    small_caves_twice = False
					
		# Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False
        visited_n[u] = visited_n[u] - 1 

	# Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

		# Mark all the vertices as not visited
        visited =[False]*(self.V)
        visited_n = np.zeros(self.V)

        small_caves_twice = False
        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path,visited_n,small_caves_twice)

cave_system2 = Graph4(number_of_caves)
for line in input:
    cave1 = line[0]
    cave2 = line[1]

    if cave1 == "start":
        cave_system2.addEdge(letter_to_number[cave1],letter_to_number[cave2])
    elif cave2 == "start":
        cave_system2.addEdge(letter_to_number[cave2],letter_to_number[cave1])
    elif cave1 == "end":
        cave_system2.addEdge(letter_to_number[cave2],letter_to_number[cave1])
    elif cave2 == "end":
        cave_system2.addEdge(letter_to_number[cave1],letter_to_number[cave2])
    else:
        cave_system2.addEdge(letter_to_number[cave1],letter_to_number[cave2])
        cave_system2.addEdge(letter_to_number[cave2],letter_to_number[cave1])

cave_system2.printAllPaths(letter_to_number["start"], letter_to_number["end"])
print("Part 2: " + str(cave_system2.total_sum))