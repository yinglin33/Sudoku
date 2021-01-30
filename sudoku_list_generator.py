import numpy as np

def output_list(str_num):
    i = 0
    sudoku_list = [[], [], [], [], [], [], [], [], []]
    for list in sudoku_list:
        for num in str_num[i:i+9]:
            if len(list) < 10:
                list.append(int(num))
        i += 9
    return sudoku_list

if __name__ == "__main__":
    print(output_list("295743861431865900876192543387459216612387495549216738763534189928671354154938600"))
