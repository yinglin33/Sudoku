import numpy as np
from sudoku_solver import solve, is_possible
from random import randint
from sudoku_list_generator import output_list
import time

def num_solutions(sudoku_board):
    list_counter = []
    def helper(board):
        if 0 not in sudoku_board:
            return True
        for i in range(9): #going through the whole board
            for j in range(9):
                if sudoku_board[i][j] == 0:
                    for k in range(1, 10):
                        if is_possible(sudoku_board, i, j, k):
                            sudoku_board[i][j] = k
                            if helper(sudoku_board):
                                list_counter.append(1)
                            sudoku_board[i][j] = 0
                    return False
    helper(sudoku_board)
    return len(list_counter)

def create_filled_board():
    board = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                    [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                    [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]])
    for number in range(1, 10):
        num, i , j = number, randint(0, 8), randint(0, 8)
        while not is_possible(board, i, j, num) or board[i][j] != 0:
            i , j = randint(0, 8), randint(0, 8)
        board[i][j] = num
    solve(board)
    return board

def create_board(filled_board):
    x = 0
    while x < 51:
        if x < 20:
            i, j = randint(0, 8), randint(0, 8)
            while filled_board[i][j] == filled_board[j][i] == 0:
                i, j = randint(0, 8), randint(0, 8)
            placeholder_one = filled_board[i][j]
            placeholder_two = filled_board[j][i]
            filled_board[i][j] = 0
            filled_board[j][i] = 0
            if num_solutions(filled_board) == 1:
                x += 2
            else:
                filled_board[i][j] = placeholder_one
                filled_board[j][i] = placeholder_two
        else:
            i, j = randint(0, 8), randint(0, 8)
            while filled_board[i][j] == 0:
                i, j = randint(0, 8), randint(0, 8)
            placeholder = filled_board[i][j]
            filled_board[i][j] = 0
            if num_solutions(filled_board) == 1:
                x += 1
            else:
                filled_board[i][j] = placeholder
        print(x)
    return filled_board

if __name__ == "__main__":
    start_time = time.time()
    x = 0
    while x < 10:
        print(create_board(create_filled_board()))
        x += 1
        print("\n" + str(x) + "\n")
    #print(num_solutions(np.array(output_list("100050079400029300089000000014030000600000040095084002800000560300700900070060420"))))
    print("My program took and average of", (time.time() - start_time) / 10, "to run")
