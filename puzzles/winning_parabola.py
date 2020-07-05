import time
import math
import numpy as np
from collections import defaultdict
#
# angles = np.arange(0.1, 90.1, 0.1)
# speeds = np.arange(0.1, 80.1, 0.1)
#
# n = int(input())
# inp = []
# for i in range(n):
#     inp.append(int(j) for j in input().split())
#
# combs = ((a,v) for a in angles for v in speeds)
#
# res = defaultdict(list)
# for x, y in inp:
#     for a in angles:
#         for v in speeds:
#             y_calc = (((-9.81*(x**2))/(2*(v**2)*(math.cos(math.radians(a))**2)))+(x*(math.tan(math.radians(a))))+1.80)
#             res[(a, v)].append(abs(y-y_calc))
#             # if math.isclose(y,
#             #                 (((-9.81*(x**2))/(2*(v**2)*(math.cos(math.radians(a))**2)))+(x*(math.tan(math.radians(a))))+1.80),
#             #                 rel_tol=1e-4):
#             #     print(a, v)
#
#     # min_key = (min(res, key=res.get))
#     # print(min_key, res[min_key])
#
# min_key = (min(res, key=(lambda x: sum(res[x]))))
# print(' '.join('{0:.1f}'.format(i) for i in min_key))
# print(min_key, res[min_key])
#
#
# # a = 61.8
# # v = 21.5
# # x = 30
# # print(((-9.81*(x**2))/(2*(v**2)*(math.cos(math.radians(a))**2)))+(x*(math.tan(math.radians(a))))+1.80)




import itertools

angles = np.arange(0.1, 90.1, 0.1)
speeds = np.arange(0.1, 80.1, 0.1)
inp, res = [], defaultdict(list)

n = int(input())
[inp.append(int(j) for j in input().split()) for i in range(n)]

start = time.time()

for i, (x, y) in enumerate(inp):
    loopstart = time.time()
    print(x,y)
    [res[(a, v)].append(abs(y-(((-9.81*(x**2))/(2*(v**2)*(math.cos(math.radians(a))**2)))+(x*(math.tan(math.radians(a))))+1.80)))\
        for a in angles for v in speeds]
    min_key = (min(res, key=(lambda x: res[x][i])))
    print(min_key, res[min_key])
    loopend = time.time()
    print('loop{}='.format(i), time.strftime("%H:%M:%S", time.gmtime(loopend - loopstart)))

# print(' '.join(map(str, min(res, key=(lambda x: sum(res[x]))))))
compute = time.time()
print(time.strftime("%H:%M:%S",time.gmtime(compute-start)))
print(' '.join(['{0:.1f}'.format(i) for i in min(res, key=(lambda x: sum(res[x])))]))
end = time.time()
print(time.strftime("%H:%M:%S",time.gmtime(end-compute)))
print(time.strftime("%H:%M:%S",time.gmtime(end-start)))