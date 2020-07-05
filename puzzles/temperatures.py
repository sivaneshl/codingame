import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
t = [0]
[t.append(int(i)) for i in input().split()]
if len(t) <= 1:
    print(0)
else:
    t = sorted(t)
    # print(t)
    index_zero = t.index(0)
    if index_zero == 0:
        print(t[index_zero+1])
    elif index_zero == len(t):
        print(t[index_zero-1])
    else:
        if t[index_zero+1]+t[index_zero-1] == 0:
            print(t[index_zero+1])
        else:
            print(t[index_zero + 1] if t[index_zero+1]-0 < 0-t[index_zero-1] else t[index_zero - 1])

