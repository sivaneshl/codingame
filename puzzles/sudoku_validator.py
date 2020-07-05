# You get a sudoku grid from a player and you have to check if it has been correctly filled.
#
# A sudoku grid consists of 9×9 = 81 cells split in 9 sub-grids of 3×3 = 9 cells.
# For the grid to be correct, each row must contain one occurrence of each digit (1 to 9), each column must contain one
# occurrence of each digit (1 to 9) and each sub-grid must contain one occurrence of each digit (1 to 9).
#
# You shall answer true if the grid is correct or false if it is not.
# Input
# 9 rows of 9 space-separated digits representing the sudoku grid.
# Output
# true or false
# Constraints
# For each digit n in the grid: 1 ≤ n ≤ 9.
# Example
# Input
# 1 2 3 4 5 6 7 8 9
# 4 5 6 7 8 9 1 2 3
# 7 8 9 1 2 3 4 5 6
# 9 1 2 3 4 5 6 7 8
# 3 4 5 6 7 8 9 1 2
# 6 7 8 9 1 2 3 4 5
# 8 9 1 2 3 4 5 6 7
# 2 3 4 5 6 7 8 9 1
# 5 6 7 8 9 1 2 3 4
# Output
# true

from itertools import chain

grid = []
for i in range(9):
    line = []
    for j in input().split():
        n = int(j)
        line.append(n)
    grid.append(line)

# print(grid)

check = list(range(1,10))
res = True

for row in grid:
    if sorted(row)!=check:
        res=False
        break

for col in list(zip(*grid)):
    if sorted(list(col))!=check:
        res=False
        break

for i in range(0,9,3):
    lsts = list(row[i:i+3] for row in grid[i:i+3])
    if sorted(list(chain(lsts[0],lsts[1],lsts[2])))!=check:
        res=False
        break

print(res)