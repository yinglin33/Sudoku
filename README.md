# Python Sudoku Solver/Generator

## Functionality:
### What It Does:
Solves a given Sudoku board layout or generates a unique Sudoku board layout.

### How It Works:
- Solver: uses a backtracking algorithm to go through, fill in numbers, and check to make sure board is valid
- Generator: uses the solver to generate a sudoku board that is unique (only one solution)

### Necessary Packages:
Numpy (follow below link's instructions to install numpy)
https://numpy.org/install/

## How To Use It:
### Solver:
For a sudoku puzzle like the following...

<img src='sudoku_image.png' title='example image' align ="center" width='750' alt='example image' >

Run the following line of code (the argument represents the board row by row, with 0's representing blanks)
```
python3 sudoku_solver.py 530070000600195000098000060800060003400803001700020006060000280000419005000080079
```

### Generator:
```
python3 sudoku_generator.py
```

## Potential Additional Features
- adding in image processing capabilities so a given image of the puzzle can be directly solved
- adding gui to create an actual playable game
- creating more efficient algorithm to generate a game with 27 blank spots
- changing algorithm to follow the rules/ideas given by the following paper
    - https://www.sudokuwiki.org/sudoku_creation_and_grading.pdf

## Citation
"Sudoku Puzzle" by Tim Stellmach is licensed under [CC0 1.0 Universal Public Domain Dedication][1]

[1]: <https://creativecommons.org/publicdomain/zero/1.0/deed.en> "CC License"
