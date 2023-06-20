import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
v1,v2 = map(int, sys.stdin.readline().split())

def dijkstra(graph, start, A):
    INF = int(1e9)
    distance = [INF for _ in range(len(graph))]
    heap = [(0,start)]
    answer = [INF for _ in range(len(A))]
    while heap:
        cost, vertex = heapq.heappop(heap)
        if distance[vertex] >= cost:
            distance[vertex] = cost
            for i in range(len(A)):
                if vertex == A[i]:
                    answer[i] = cost
                    for j in range(len(A)):
                        if answer[j] == INF:
                            break
                    else:
                        return answer
            for G in graph[vertex]:
                if distance[G[1]] > G[0]+cost:
                    distance[G[1]] = G[0]+cost
                    heapq.heappush(heap,(G[0]+cost, G[1]))
    return answer

r_graph = [[0  for _ in range(4)] for _ in range(4)]
s_v1, s_v2 = dijkstra(graph, 1, [v1,v2])
v1_v2, v1_V = dijkstra(graph, v1, [v2,V])
v2_V = dijkstra(graph, v2, [V])
INF = int(1e9)
answer = min(s_v1+v1_v2+v2_V[0], s_v2+v1_v2+v1_V)
if answer >= INF:
    print(-1)
else:
    print(answer)