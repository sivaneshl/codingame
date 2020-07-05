# Goal
# THEY put you in a square shape room, with N meters on each side.
# THEY want to know everything about you.
# THEY are observing you.
# THEY placed some candles in the room.
#
# Every candle makes L "light" in the spot they are, and every spot in square shape gets one less "light" as the next
# ones. If a spot is touched by two candles, it will have the larger "light" it can have. Every spot has the base light
# of 0.
#
# You can hide only, if you find a dark spot which has 0 "light".
# How many dark spots you have?
#
# You will receive a map of the room, with the empty places (X) and Candles (C) in N rows, each character separated by
# a space.
#
# Example for the light spread N = 5, L = 3:
# X X X X X
# X C X X X
# X X X X X
# X X X X X
# X X X X X
#
# 2 2 2 1 0
# 2 3 2 1 0
# 2 2 2 1 0
# 1 1 1 1 0
# 0 0 0 0 0
#
# Input
# Line 1: An integer N for the length of one side of the room.
# Line 2: An integer L for the base light of the candles.
# Next N lines: N number of characters (as c), separated by one space.
#
# Output
# Line 1 : The number of places with zero light.
#
# Constraints
# 0 < N <= 25
# 0 < L < 10
#
# Example
# Input
# 5
# 3
# X X X X X
# X C X X X
# X X X X X
# X X X X X
# X X X X X
# Output
# 9

import numpy as np
import itertools

n = int(input())
l = int(input())

lines = [(input().split()) for i in range(n)]

c_pos_list = [[x, y] for x, line in enumerate(lines) for y, value in enumerate(line) if value=='C']
print(c_pos_list)

# c_pos_list.append([2,2])
main = set(list(itertools.product(range(n), range(n))))
zero_list = []
res = main
for i, (cx, cy) in enumerate(c_pos_list):
    lx_start, lx_end = 0 if cx-l < 0 else cx-l+1, n if cx+l > n else cx+l
    ly_start, ly_end = 0 if cy-l < 0 else cy-l+1, n if cy+l > n else cy+l
    print((cx, cy), lx_start, lx_end, ly_start, ly_end)
    zeros = sorted(set(main) - set(list(itertools.product(range(lx_start, lx_end), range(ly_start, ly_end)))))
    print(zeros)
    zero_list.append(zeros)
    res = res.intersection(zeros)

print(zero_list) # need to get the common elements from each list in zero_list
print(len(zero_list))
print(res)
print(len(res))
