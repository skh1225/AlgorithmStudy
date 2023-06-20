import sys
input = sys.stdin.readline
import heapq


T = int(input())
for _ in range(T):
    N, M, K = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    distance = [[int(1e5) for _ in range(M+1)] for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d = map(int,input().split())
        graph[u].append((c,d,v))
    heap = [(0,0,1)]
    while heap:
        c,t,x = heapq.heappop(heap)
        if t < distance[x][0]:
            distance[x][0] = t
            for G in graph[x]:
                n_c,n_t,n_x = G
                if c+n_c <= M and t+n_t < distance[n_x][c+n_c] and t+n_t < distance[n_x][0]:
                    distance[n_x][c+n_c] = t+n_t
                    heapq.heappush(heap, (c+n_c,t+n_t,n_x))
    if distance[N][0] == int(1e5):
        print("Poor KCM")
    else:
        print(distance[N][0])