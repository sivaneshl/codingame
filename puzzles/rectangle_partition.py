# Goal
# There is a rectangle of given width w and height h,
#
# On the width side, you are given a list of measurements.
# On the height side, you are given another list of measurements.
#
# Draw perpendicular lines from the measurements to partition the rectangle into smaller rectangles.
#
# In all sub-rectangles (include the combinations of smaller rectangles), how many of them are squares?
#
#
# Example
#
# w = 10
# h = 5
# measurements on x-axis: 2, 5
# measurements on y-axis: 3
#
#    ___2______5__________
#   |   |      |          |
#   |   |      |          |
#  3|___|______|__________|
#   |   |      |          |
#   |___|______|__________|
#
# Number of squares in sub-rectangles = 4 (one 2x2, one 3x3, two 5x5)
# Input
# Line 1: Integers w h countX countY, separated by space
# Line 2: list of measurements on the width side, countX integers separated by space, sorted in asc order
# Line 3: list of measurements on the height side, countY integers separated by space, sorted in asc order
# Output
# Line 1: the number of squares in sub-rectangles created by the added lines
# Constraints
# 1 ≤ w, h ≤ 20,000
# 1 ≤ number of measurements on each axis ≤ 500
# Example
# Input
# 10 5 2 1
# 2 5
# 3
# Output
# 4

from operator import sub
import itertools
import time
import pandas as pd

def get_common(l1, l2):
    pools = [tuple(pool) for pool in (l1, l2)]
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        if prod[0]==prod[1]:
            yield tuple(prod)

w, h, count_x, count_y = [int(i) for i in input().split()]
x_cut_list, y_cut_list, x_boxes, y_boxes = [0, w], [0, h], [], []
[x_cut_list.append(int(i)) for i in input().split()]
[y_cut_list.append(int(i)) for i in input().split()]
start = time.time()
[x_boxes.append(sub(*pair)) for pair in itertools.combinations(sorted(x_cut_list, reverse=True), r=2)]
[y_boxes.append(sub(*pair)) for pair in itertools.combinations(sorted(y_cut_list, reverse=True), r=2)]
compute = time.time()
print(time.strftime("%H:%M:%S",time.gmtime(compute-start)))
x_boxes = sorted(x_boxes)
y_boxes = sorted(y_boxes)
print(x_boxes, y_boxes)

# Option 1 - double loop
# print(len([x for x in x_boxes for y in y_boxes if x==y]))

# option 2 - get the count of each value thus eliminating duplicates in order to reduce the number of loop iterations
# and for each match multiply the count of occurrences and add them all
x_counts = pd.Series(x_boxes).value_counts().to_dict()
y_counts = pd.Series(y_boxes).value_counts().to_dict()
sort = time.time()
print(time.strftime("%H:%M:%S",time.gmtime(sort-compute)))
print(sum([x_counts[x]*y_counts[y] for x in x_counts for y in y_counts if x==y]))

# out=0
# for x in x_counts:
#     for y in y_counts:
#         if x==y:
#             out+=x_counts[x]*y_counts[y]
# print(out)

# Option 3 -count the occurrences of common item in 2nd list and add them all
print(sum([y_boxes.count(i) for i in x_boxes]))

end = time.time()
print(time.strftime("%H:%M:%S",time.gmtime(end-compute)))
print(time.strftime("%H:%M:%S",time.gmtime(end-start)))

