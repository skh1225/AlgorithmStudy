import sys
import heapq

INF = int(1e7)
V, E = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]
distance = [INF for _ in range(V+1)]
start = int(sys.stdin.readline())
for i in range(E):
    x,y,cost = map(int,sys.stdin.readline().split())
    graph[x].append([cost, y])
heap = [[0,start]]

while heap:
    cost, des = heapq.heappop(heap)
    if distance[des] < cost:
        continue
    distance[des] = cost
    for G in graph[des]:
        if G[0]+cost < distance[G[1]]:
            distance[G[1]] = G[0]+cost
            heapq.heappush(heap, [G[0]+cost, G[1]])

for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])