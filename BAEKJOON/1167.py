import sys
input = sys.stdin.readline
from collections import deque

V = int(input())
graph = [[] for _ in range(V+1)]
radius = [0 for _ in range(V+1)]
degree = [0 for _ in range(V+1)]
leaves = deque([])
answer = 0

for _ in range(V):
    tpl = tuple(map(int, input().split()))
    for i in range(1,len(tpl)//2):
        graph[tpl[0]].append((tpl[i*2-1],tpl[i*2]))
    degree[tpl[0]] = len(tpl)//2-1
    if degree[tpl[0]] == 1:
        leaves.append(tpl[0])
    
while leaves:
    leaf = leaves.popleft()
    for v,c in graph[leaf]:
        if degree[v] > 0:
            answer = max(answer, radius[leaf]+c+radius[v])
            radius[v] = max(radius[v], radius[leaf]+c)
            degree[v] -= 1
            degree[leaf] -= 1
            if degree[v] == 1:
                leaves.append(v)

print(answer)
