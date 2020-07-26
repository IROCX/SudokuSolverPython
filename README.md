# SudokuSolverPython
A simple python script to solve sudoku for you.

This illustrates a simple 9x9 Sudoku Solving algorithm python script.

It uses a possible() function to check the row, column and 3x3 square corresponding to the current block for a number n.

Function possible is then incorporated in another function solver() which goes through the grid and searches for 0s that represent empty blocks.
It then tries all the numbers 1 through 9 for a particular empty block and selects a possible value x for it. It then solves the grid recursively 
for that selection of x for that block.
If it reaches dead end it makes the block 0 again and checks for next block containing 0 and solves the entire grid again for 
a selection of x for that block.

As a result, at the end we wil get a solved Sudoku certainly.
