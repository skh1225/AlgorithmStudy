import sys
input = sys.stdin.readline
from collections import deque
N, P = map(int, input().split())

cap = [[0 for _ in range(N+1)] for _ in range(N+1)]
flow = [[0 for _ in range(N+1)] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(P):
    x, y = map(int, input().split())
    graph[x].append(y); graph[y].append(x)
    cap[x][y] += 1

def bfs():
    queue = deque([1])
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if not visited[y] and cap[x][y] > flow[x][y]:
                visited[y] = x
                queue.append(y)
                if y == 2:
                    return True
    return False

def make_flow():
    curr = 2
    min_flow = N
    while curr != 1:
        prev = visited[curr]
        min_flow = min(min_flow, cap[prev][curr]-flow[prev][curr])
        curr = prev
    curr = 2
    while curr != 1:
        prev = visited[curr]
        flow[prev][curr] += min_flow
        flow[curr][prev] -= min_flow
        curr = prev
    return min_flow

answer = 0
while True:
    visited = [0 for _ in range(N+1)]
    if not bfs():
        break
    answer += make_flow()
print(answer)