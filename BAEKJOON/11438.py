import sys
input = sys.stdin.readline
from math import ceil, log2
from collections import deque

N = int(input())
LOG = ceil(log2(N))+1

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

depth = [0 for _ in range(N+1)]
parents = [[0 for _ in range(LOG)] for _ in range(N+1)]

def bfs():
    queue = deque([(1,1)])
    while queue:
        node, d = queue.popleft()
        depth[node] = d
        for G in graph[node]:
            if not depth[G]:
                queue.append((G,d+1))
                parents[G][0] = node

def set_parents():
    bfs()
    for i in range(1,LOG):
        for j in range(1,N+1):
            if depth[j] <= 2**i:
                continue
            parents[j][i] = parents[parents[j][i-1]][i-1]

def lca(a,b):
    if depth[a] > depth[b]:
        a, b = b, a
    diff = depth[b]-depth[a]
    while diff > 0:
        b = parents[b][int(log2(diff))]
        diff = depth[b]-depth[a]
    while a != b:
        for i in range(LOG):
            if parents[a][i] == parents[b][i]:
                break
        if i == 0:
            a, b = parents[a][0], parents[b][0]
            break
        else:
            a, b = parents[a][i-1], parents[b][i-1]
    print(a)

set_parents()
M = int(input())
for _ in range(M):
    a,b = map(int, input().split())
    lca(a,b)