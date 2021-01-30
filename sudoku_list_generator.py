import numpy as np

def output_list(str_num):
    """
    Outputs a list from a string of numbers that is meant to represent a sudoku game
    board. For example, the following...

    530070000600195000098000060800060003400803001700020006060000280000419005000080079

    will turn into...

    [[5 3 0 0 7 0 0 0 0]
    [6 0 0 1 9 5 0 0 0]
    [0 9 8 0 0 0 0 6 0]
    [8 0 0 0 6 0 0 0 3]
    [4 0 0 8 0 3 0 0 1]
    [7 0 0 0 2 0 0 0 6]
    [0 6 0 0 0 0 2 8 0]
    [0 0 0 4 1 9 0 0 5]
    [0 0 0 0 8 0 0 7 9]]
    """
    i = 0
    sudoku_list = [[], [], [], [], [], [], [], [], []]
    for list in sudoku_list:
        for num in str_num[i:i+9]:
            if len(list) < 10:
                list.append(int(num))
        i += 9
    return sudoku_list
