import os
import numpy as np
cur_dir = os.path.dirname(os.path.abspath(__file__))

# Part 1
with open(cur_dir + "\\input_04.txt") as file:
    input = [line.splitlines() for line in file.readlines()]

numbers_drawn = input[0][0].split(",")

input_boards = input[1:]

input_boards = [[int(x) for x in line[0].split()] for line in input_boards]

boards = []

numbers_of_boards = int(len(input_boards)/6)
for nbr in range(numbers_of_boards):
    current_board = np.zeros((5,5))
    for i in range(5):
        for j in range(5):
            current_board[i, j] = input_boards[6*nbr+1+i][j]
    boards += [current_board]

board_checker = [np.zeros((5,5)) for x in range(int(len(input_boards)/6))]


def check_bingo(input_board):
    win_0 = np.any(input_board.sum(axis = 0) == 5)
    win_1 = np.any(input_board.sum(axis = 1) == 5)
    return np.any([[win_0], [win_1]])

which_board_win = None
break_out = False
win_board = None
win_board_check = None
win_number = None
for number in numbers_drawn:
    number = int(number)
    for i,board in enumerate(boards):
        board_checker[i][board == number] = 1
        if check_bingo(board_checker[i]):
            break_out = True
            win_board = board
            win_board_check = board_checker[i]
            win_number = number
            break
    if break_out:
        break


print("Part 1: " + str(win_board[np.invert(win_board_check.astype("bool"))].sum() * win_number))

# Part 2
board_checker = [np.zeros((5,5)) for x in range(int(len(input_boards)/6))]

board_wins = [np.zeros(1, dtype = bool) for x in range(numbers_of_boards)]
which_board_win = None
break_out = False
win_board = None
win_board_check = None
win_number = None
for number in numbers_drawn:
    number = int(number)
    for i,board in enumerate(boards):
        board_checker[i][board == number] = 1
        if check_bingo(board_checker[i]):
            board_wins[i] = [True]
            if np.all(board_wins):
                break_out = True
                win_board = board
                win_board_check = board_checker[i]
                win_number = number
                break
    if break_out:
        break

print("Part 2: " + str(win_board[np.invert(win_board_check.astype("bool"))].sum() * win_number))
