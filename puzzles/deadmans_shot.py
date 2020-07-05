#  	Goal
# Captain Jack Sparrow and his pirate friends have been drinking one night. After plenty of rum, they got into an
# argument about who is the best shot. Captain Jack takes up some paint and paints a target on a nearby wall. The
# pirates take out their guns and start shooting.
#
# Your task is to help the drunk pirates find out which shots hit the target.
#
# Captain Jack Sparrow drew the target by drawing N lines. The lines form a convex shape defined by N corners. A convex
# shape has all internal angles less than 180 degrees. For example, all internal angles in a square are 90 degrees.
#
# A shot within the convex shape or on one of the lines is considered a hit.
# Input
# Line 1: An integer N for the number of corners.
# Next N lines: Two space-separated integers x and y for the coordinates of a corner. The corners are listed in a
# counterclockwise manner. The target is formed by connecting the corners together with lines and connecting the last
# corner with the first one.
# Line N+1: An integer M for the number of shots.
# Next M lines: Two space-separated integers x and y for the coordinates of each shot.
# Output
# M lines with either "hit" or "miss" depending on whether the shot hit the target or not.
# Constraints
# 3 ≤ N ≤ 10
# 1 ≤ M ≤ 10
# -10000 < x,y < 10000
# Example
# Input
# 4
# -100 -100
# 100 -100
# 100 100
# -100 100
# 5
# 0 0
# 99 99
# 101 101
# 80 -101
# 0 -100
# Output
# hit
# hit
# miss
# miss
# hit

n = int(input())
shape = [[int(j) for j in input().split()] for i in range(n)]
m = int(input())
shots = [[int(j) for j in input().split()] for i in range(m)]

def shot_in_shape(x, y):
    n = len(shape)
    inside = False

    p1x, p1y = shape[0]
    for i in range(1,n+1):
        p2x, p2y = shape[i%n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

for shot in shots:
    print('hit' if shot_in_shape(shot[0], shot[1]) else 'miss')