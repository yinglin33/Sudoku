import numpy as np
from sudoku_list_generator import output_list

def good_row(sudoku_board, row_num, num):
    rows = [sudoku_board[i, :] for i in range(9)]
    if num not in rows[row_num]:
        return True
    return False

def good_col(sudoku_board, col_num, num):
    cols = [sudoku_board[:, i] for i in range(9)]
    if num not in cols[col_num]:
        return True
    return False

def good_box(sudoku_board, row_num, col_num, num):
    boxes = [sudoku_board[3 * i: 3 * (i + 1), 3 * j: 3 * (j + 1)] for i in range(3) for j in range(3)]
    if num not in boxes[(row_num // 3) * 3 + (col_num // 3)]:
        return True
    return False

def is_possible(sudoku_board, row_num, col_num, num):
    return good_row(sudoku_board, row_num, num) and good_col(sudoku_board, col_num, num) and good_box(sudoku_board, row_num, col_num, num)

def solve(sudoku_board):
    if 0 not in sudoku_board:
        return True
    for i in range(9): #going through the whole board
        for j in range(9):
            if sudoku_board[i][j] == 0:
                for k in range(1, 10):
                    if is_possible(sudoku_board, i, j, k):
                        sudoku_board[i][j] = k
                        if solve(sudoku_board):
                            return True
                        sudoku_board[i][j] = 0
                return False


if __name__ == "__main__":
    board = np.array(output_list("530070000600195000098000060800060003400803001700020006060000280000419005000080079"))
    print(board)
    solve(board)
    print(board)
