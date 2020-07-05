# Goal
# Ghost Legs is a kind of lottery game common in Asia. It starts with a number of vertical lines. Between the lines
# there are random horizontal connectors binding all lines into a connected diagram, like the one below.
#
# A  B  C
# |  |  |
# |--|  |
# |  |--|
# |  |--|
# |  |  |
# 1  2  3
#
# To play the game, a player chooses a line in the top and follow it downwards. When a horizontal connector is
# encountered, he must follow the connector to turn to another vertical line and continue downwards. Repeat this until
# reaching the bottom of the diagram.
#
# In the example diagram, when you start from A, you will end up in 2. Starting from B will end up in 1. Starting from
# C will end up in 3. It is guaranteed that every top label will map to a unique bottom label.
#
# Given a Ghost Legs diagram, find out which top label is connected with which bottom label. List all connected pairs.
# Input
# Line 1: Integer W and H for width and height of the diagram below.
# Next H lines: Containing a Ghost Legs diagram as your input.
#
# The diagram itself is composed of characters: '|' and '-', (and space).
# The top line in the diagram has a number of labels T.
# The bottom line contains labels B.
#
# Each T and B is a single ascii character that can be of any random value.
# Do not assume they will always be ABC or 123.
#
# As a rule of the game, left and right horizontal connectors will never appear at the same point.
#
# All diagrams are having the same style as the test cases.
# Output
# List all connected pairs between top and bottom labels, TB, in the order of the top labels from Left to Right.
# Write each pair in a separate line.
# Constraints
# 3 < W, H ≤ 100
#
# Example
# Input
# 7 7
# A  B  C
# |  |  |
# |--|  |
# |  |--|
# |  |--|
# |  |  |
# 1  2  3
# Output
# A2
# B1
# C3

w, h = [int(i) for i in input().split()]
diagram = []
for i in range(h):
    line = input()
    diagram.append(line)

for i, lines in enumerate(diagram):
    print(i, lines)

lines = diagram
output = ''
# # for i, lines in enumerate(diagram):
for k in range(w):
    i = 0
    if k%3==0:
        j = k
    else:
        continue
    for i in range(h):
        if i == 0:
            output += lines[i][j]
            # print('first = ', i, j, lines[i][j])
        if i == h-1:
            output += lines[i][j] + " "
            # print("last = ", i, j, lines[i][j])
            # print(output)

        # print(i,j)
        # print(lines[i][j], lines[i][j+1])
        if j<(w-1) and lines[i][j+1] == '-':
            j += 3
            # print("j+2=", j)
        elif lines[i][j-1] == '-':
            j -= 3
            # print("j-2=", j)


for out in output.split():
    print(out)