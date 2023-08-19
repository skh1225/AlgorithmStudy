import sys
input = sys.stdin.readline
from math import ceil
INF = int(1e5)
t = lambda x: ord(x)-ord('A') if x <= 'Z' else ord(x)-ord('a')+26

N = int(input())
graph = [[] for _ in range(52)]
cap = [[0 for _ in range(52)] for _ in range(52)]
flow = [[0 for _ in range(52)] for _ in range(52)]
for _ in range(N):
    x,y,f = input().split()
    x,y,f = t(x), t(y), int(f)
    graph[x].append(y); graph[y].append(x)
    cap[x][y] += f; cap[y][x] += f

def bfs():
    queue = [0]
    for x in queue:
        for y in graph[x]:
            if visited[y] < 0 and cap[x][y] > flow[x][y]:
                visited[y] = x
                queue.append(y)
                if y == 25:
                    return make_flow()
    return 0

def make_flow():
    min_flow = INF
    curr = 25
    while curr != 0:
        min_flow = min(min_flow, cap[visited[curr]][curr]-flow[visited[curr]][curr])
        curr = visited[curr]
    curr = 25
    while curr != 0:
        flow[visited[curr]][curr] += min_flow
        flow[curr][visited[curr]] -= min_flow
        curr = visited[curr]
    return min_flow

answer = 0
while True:
    visited = [-1 for _ in range(52)]
    cost = bfs()
    if not cost:
        break
    answer += cost
print(answer)