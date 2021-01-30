import numpy as np
from sudoku_solver import solve, is_possible
from random import randint
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
    """
    Creates a sudoku board so that only 30 empty spots are generated
    and only one solution is possible.
    """
    x = 0
    while x < 51: #stops when 51 spots out of 81 are filled
        if x < 20: #adds numbers two at a time for first 20 numbers
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
    print(create_board(create_filled_board()))
