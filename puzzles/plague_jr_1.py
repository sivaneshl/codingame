from itertools import chain
from random import choice
import sys
sys.setrecursionlimit(2000)


n = int(input())
edges = [[int(j) for j in input().split()] for i in range(n)]
nodes = list(set(node for node in chain(*edges)))
paths = dict((n, []) for n in nodes)

for s, e in edges:
    paths[s].append(e)
    paths[e].append(s)

def find_all_paths(start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in paths:
        return []
    all_paths = []
    for node in paths[start]:
        if node not in path:
            add_path = find_all_paths(node, end, path)
            for p in add_path:
                all_paths.append(p)
    return all_paths

def get_finals(vs):
    for e in vs:
        for x in (set(chain(*list((s1, e1) for s1, e1 in edges if (e1 == e or s1 == e))))):
            if x not in vs:
                vs.append(x)
    print(vs)
    if vs[-1] not in final_nodes:
        final_nodes.append(vs[-1])

final_nodes = []
i = 0
while len(final_nodes)<2 and i<10:
    vs = [choice(nodes)]
    get_finals(vs)
    i += 1


print(final_nodes)
if len(final_nodes)==1:
    final_nodes.append(choice(nodes))
print(len(find_all_paths(final_nodes[0], final_nodes[1]))//2)


