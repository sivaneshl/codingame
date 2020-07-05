# You're given a grid filled with 0 and #, where 0 represents a passage, and # represents a wall: an impassable cell.
#
# We're considering the 4-adjacency, meaning a cell has a maximum of 4 adjacent cells (a diagonal cell is not adjacent).
#
# You must analyze the given grid and return it with a small transformation:
# For each empty cell, instead of a 0, you must return the number of its adjacent passable cells.
# For each impassable cell, you change nothing: you still return #.
# Game Input
# First line: 2 integers width and height for the size of the grid.
# Next height lines: a string line of length width where 0 is a passage and # is a wall.
# The maze is enclosed in impassable rocks that are not included in the data.
# Game Output
# height line of width characters each containing the transformed grid.
# Constraints
# 1 ≤ width & height ≤ 100
#
# Allotted response time to output is = 2s

width, height = [int(i) for i in input().split()]
grid, grid2 = [], []
for i in range(height):
    line = input()
    grid.append(line)

n = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for x in range(height):
    print(''.join([str(len([(x+a[0], y+a[1]) for a in n if ((0 <= x+a[0] < height) and (0 <= y+a[1] < width) and grid[x+a[0]][y+a[1]]!='#')]))
                  if grid[x][y] != '#' else '#' for y in range(width)]))





