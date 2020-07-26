import numpy as np

def possible(x, y, n):
    global example
    for i in range(0,9):
        if example[x][i] == n:
            return False
    for i in range(0,9):
        if example[i][y] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3

    for i in range(0,3):
        for j in range(0,3):
            if example[x0+i][y0+j]==n:
                return False
    return True

def solver(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for k in range(1,10):
                    if possible(i,j,k):
                        grid[i][j] = k
                        solver(grid)
                        grid[i][j] = 0
                return
    print(np.matrix(grid))


example = []
print("Input Sudoku : ")

for i in range(9):
    arr = list(map(int, input().split()))
    example.append(arr)

print()
print("Problem Sudoku : ")
print(np.matrix(example))
print()

print("Solution Sudoku : ")
solver(example)
