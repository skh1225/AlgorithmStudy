import sys
input = sys.stdin.readline

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
        prev = visited[curr]
        min_flow = min(min_flow, cap[prev][curr]-flow[prev][curr])
        curr = prev
    curr = 25
    while curr != 0:
        prev = visited[curr]
        flow[prev][curr] += min_flow
        flow[curr][prev] -= min_flow
        curr = prev
    return min_flow

answer = 0
while True:
    visited = [-1 for _ in range(52)]
    cost = bfs()
    if not cost:
        break
    answer += cost
print(answer)