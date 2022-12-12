import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_02.txt") as file:
    strategy = [line.strip().split(" ") for line in file.readlines()]

point_dict = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
encryption = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

points = 0
for round in range(len(strategy)):
    curr_points = 0
    opponent = strategy[round][0]
    me = strategy[round][1]
    if encryption[opponent] == me:
        curr_points += 3
    elif opponent == "A" and me == "Y":
        curr_points += 6
    elif opponent == "B" and me == "Z":
        curr_points += 6
    elif opponent == "C" and me == "X":
        curr_points += 6
    
    curr_points += point_dict[me]
    points += curr_points

print("Part 1: " + str(points))

# Part 2
what_wins_against_opp = {
    "A" : "Y",
    "B" : "Z",
    "C" : "X"
}
what_loses_against_opp = {
    "A" : "Z",
    "B" : "X",
    "C" : "Y"
}
win_draw_lose = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

points = 0
for round in range(len(strategy)):
    curr_points = 0
    opponent = strategy[round][0]
    me = strategy[round][1]
    what_i_choose = ""
    if me == "X": #lose
        what_i_choose = what_loses_against_opp[opponent]
    elif me == "Z": #win
        what_i_choose = what_wins_against_opp[opponent]
    elif me == "Y": #draw
        what_i_choose = encryption[opponent]
    curr_points += point_dict[what_i_choose]
    curr_points += win_draw_lose[me]
    points += curr_points

print("Part 2: " + str(points))

