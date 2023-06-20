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
    cap[x][y] = 1; cap[y][x] = 1

def bfs():
    queue = deque([1])
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if not pre[y] and cap[x][y] > flow[x][y]:
                if not visited[pre[x]] and visited[x] and flow[x][y] != -1:
                    continue
                pre[y] = x
                queue.append(y)
                if y == 2:
                    return True
    return False

def make_flow():
    curr = 2
    min_flow = N
    while curr != 1:
        min_flow = min(min_flow, cap[pre[curr]][curr]-flow[pre[curr]][curr])
        curr = pre[curr]
    curr = 2
    while curr != 1:
        print(curr)
        flow[pre[curr]][curr] += min_flow
        flow[curr][pre[curr]] -= min_flow
        if flow[pre[curr]][curr] == 0:
            visited[curr] = False
        else:
            visited[curr] = True
        curr = pre[curr]
    return min_flow

answer = 0
visited = [False for _ in range(N+1)]
while True:
    pre = [0 for _ in range(N+1)]
    if not bfs():
        break
    answer += make_flow()
print(answer)