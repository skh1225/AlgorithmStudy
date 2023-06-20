import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((c,b))

start, end = map(int,sys.stdin.readline().split())

def dijkstra(graph,N,start,end):
    INF = int(1e8)
    distance = [INF for _ in range(N+1)]
    heap = [(0, start)]
    while heap:
        cost, city = heapq.heappop(heap)
        if city == end:
            return cost
        if distance[city] < cost:
            continue
        distance[city] = cost
        for G in graph[city]:
            n_cost,n_city = G
            if n_cost+cost < distance[n_city]:
                heapq.heappush(heap,(n_cost+cost,n_city))
                distance[n_city] = n_cost+cost
print(dijkstra(graph,N,start,end))