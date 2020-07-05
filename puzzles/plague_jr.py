# You want to destroy humankind.
#
# To practice your humankind-destruction skills, you've set up a network of nutritive tissue pads connected with organic
# rods, such that a unique path from a pad to another always exists. You'll infect one of the pads with the Disease,
# and watch it spread. Every night, the Disease will spread from the infected pads to the adjacent non-infected pads.
#
# You are given the network structure. Assuming optimal choice for the initial Disease injection, after how many nights
# would the entire network be affected?
#
#
# Thanks to @dbdr for the choice of words.
# Input
# Line 1: N the number of rods.
# N lines: A B indices of the pads connected by that rod.
# Output
# R number of nights to total infection.
# Constraints
# The network is connected and acyclic.
# 0 ≤ A, B ≤ N < 1000
# Example
# Input
# 2
# 0 1
# 1 2
# Output
# 1

import networkx as nx
from itertools import chain
import time
import sys
import random
sys.setrecursionlimit(2000)

n = int(input())
edge_list = [[int(j) for j in input().split()] for i in range(n)]

start = time.time()
nodes = list(set(node for node in chain(*edge_list)))
paths = dict((n, []) for n in nodes)

print(len(nodes), len(edge_list))

for s, e in edge_list:
    paths[s].append(e)
    paths[e].append(s)
# print(paths)
path_time = time.time()
print(time.strftime("%H:%M:%S",time.gmtime(path_time-start)))

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

max_dia = 0
i = 0
start_node = random.choice(nodes)
while i < 2:
    loop_start = time.time()
    dist = dict((n, []) for n in nodes)
    for n in nodes:
        dist[n] = find_all_paths(start_node, n)
    max_node = max(dist, key=lambda x: len(dist[x]))
    dia = len(dist[max_node])
    if dia > max_dia:
        max_dia = dia
    print(start_node, max_node, dia)
    loop_end = time.time()
    print(time.strftime("%H:%M:%S", time.gmtime(loop_end - loop_start)))
    i+=1
    start_node = max_node

print(max_dia//2)

end = time.time()
print(time.strftime("%H:%M:%S",time.gmtime(end-start)))


# start = time.time()
# g = nx.Graph()
# g.add_edges_from(edge_list)
# p = [(max(list(nx.shortest_path_length(g, n).values()))) for n in g.nodes]
# print(min(p))
# end = time.time()
# print(time.strftime("%H:%M:%S",time.gmtime(end-start)))




