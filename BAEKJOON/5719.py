import sys
input = sys.stdin.readline
import heapq
from collections import deque

def dijkstra1(start, end):
    heap = [(0, start)]
    distance[start] = 0
    while heap:
        c,v = heapq.heappop(heap)
        if v == end:
            break
        if distance[v] == c:
            for G in graph1[v]:
                n_c, n_v = G
                if c+n_c < distance[n_v]:
                    distance[n_v] = c + n_c
                    heapq.heappush(heap, (c + n_c, n_v))

def dijkstra2(start, end, INF, N):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for G in graph2[node]:
            if G[2] and distance[node]-distance[G[1]] == G[0]:
                queue.append(G[1])
                G[2] = False
    INF = N*1000
    distance2 = [INF for _ in range(N)]
    heap = [(0,start)]
    distance2[start] = 0
    while heap:
        c,v = heapq.heappop(heap)
        if v == end:
            break
        if distance2[v] == c:
            for G in graph2[v]:
                if G[2]:
                    n_c, n_v = G[:2]
                    if c+n_c < distance2[n_v]:
                        distance2[n_v] = c + n_c
                        heapq.heappush(heap, (c + n_c, n_v))
    if distance2[end] == INF:
        print(-1)
    else:
        print(distance2[end])




while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    start, end = map(int, input().split())
    graph1, graph2 = [[] for _ in range(N)], [[] for _ in range(N)]
    INF = N*1000
    distance = [INF for _ in range(N)]
    for _ in range(M):
        u, v, c = map(int, input().split())
        graph1[u].append((c,v))
        graph2[v].append([c,u,True])
    dijkstra1(start, end)
    dijkstra2(end, start, INF, N)
    