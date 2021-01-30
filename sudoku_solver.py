import sys
import numpy as np
from sudoku_list_generator import output_list

def good_row(sudoku_board, row_num, num):
    """
    Checks to make sure that a given row in a sudoku is possible if an int
    num is placed into that row
    """
    rows = [sudoku_board[i, :] for i in range(9)]
    if num not in rows[row_num]:
        return True
    return False

def good_col(sudoku_board, col_num, num):
    """
    Checks to make sure that a given column in a sudoku board is possible if
    an int num is placed into that column
    """
    cols = [sudoku_board[:, i] for i in range(9)]
    if num not in cols[col_num]:
        return True
    return False

def good_box(sudoku_board, row_num, col_num, num):
    """
    Checks to make sure that a given "box" in a sudoku board is possible if an
    int num is placed into that "box"
    """
    boxes = [sudoku_board[3 * i: 3 * (i + 1), 3 * j: 3 * (j + 1)] for i in range(3) for j in range(3)]
    if num not in boxes[(row_num // 3) * 3 + (col_num // 3)]:
        return True
    return False

def is_possible(sudoku_board, row_num, col_num, num):
    return good_row(sudoku_board, row_num, num) and good_col(sudoku_board, col_num, num) and good_box(sudoku_board, row_num, col_num, num)

def solve(sudoku_board):
    """
    Solves the sudoku_board using a backtracking algorithm.
    """
    if 0 not in sudoku_board:
        return True
    for i in range(9): #going through the whole board
        for j in range(9):
            if sudoku_board[i][j] == 0:
                for k in range(1, 10):
                    if is_possible(sudoku_board, i, j, k):
                        sudoku_board[i][j] = k
                        if solve(sudoku_board): #recursive/backtracking step
                            return True
                        sudoku_board[i][j] = 0
                return False

if __name__ == "__main__":
    if len(sys.argv) == 2:
        board = np.array(output_list(sys.argv[1]))
        print(board)
        solve(board)
        print(board)
    else:
        print("Please enter the correct amount of arguments.")
        sys.exit()
