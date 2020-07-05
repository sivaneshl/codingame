import numpy as np
import math
from collections import defaultdict
import time

angles = np.arange(0.1, 90.1, 0.1)
speeds = np.arange(0.1, 80.1, 0.1)
inp, res = [], defaultdict(list)

n = int(input())
[inp.append(int(j) for j in input().split()) for i in range(n)]

start = time.time()

for x, y in inp:
    [res[(a, v)].append(abs(y-(((-9.81*(x**2))/(2*(v**2)*(math.cos(math.radians(a))**2)))+(x*(math.tan(math.radians(a))))+1.80)))\
        for a in angles for v in speeds]

print(' '.join(['{0:.1f}'.format(i) for i in min(res, key=(lambda x: sum(res[x])))]))
end = time.time()
print(time.strftime("%H:%M:%S",time.gmtime(end-start)))