# 문제 2
import sys
import heapq
INF = int(1e9)
N, M, C = map(int, sys.stdin.readline().split())
visited = [False]*(N+1)
visited[0] = True
distance = [INF]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([end, cost])


def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    while len(heap) > 0:
        smallest = heapq.heappop(heap)
        if visited[smallest[1]]:
            continue
        visited[smallest[1]] = True
        distance[smallest[1]] = min(distance[smallest[1]], smallest[0])
        for i in graph[smallest[1]]:
            heapq.heappush(
                heap, [min(distance[i[0]], distance[smallest[1]]+i[1]), i[0]])


dijkstra(C)
print(distance)
cnt = -1
max = 0
for idx, v in enumerate(distance):
    if v < INF:
        cnt += 1
        if v > max:
            max = v
print(cnt, max)

# # 문제 1
# import sys
# N, M = map(int, sys.stdin.readline().split())
# X, K = map(int, sys.stdin.readline().split())
# INF = int(1e9)

# # graph = [[INF]*(N+1) for _ in range(N+1)]
# # for i in range(N+1):
# #     graph[i][i] = 0

# # for _ in range(M):
# #     A, B = map(int, sys.stdin.readline().split())
# #     graph[A][B] = 1
# #     graph[B][A] = 1
# graph = [[0, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000], [1000000000, 0, 1, 1, 1, 1000000000], [1000000000, 1, 0, 1000000000,
#                                                                                                                  1, 1000000000], [1000000000, 1, 1000000000, 0, 1, 1], [1000000000, 1, 1, 1, 0, 1], [1000000000, 1000000000, 1000000000, 1, 1, 0]]

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         for k in range(1, N+1):
#             graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])
# if graph[1][K]+graph[K][X] > INF:
#     print(-1)
# else:
#     print(graph[1][K]+graph[K][X])


# 기본 구현
# import sys
# INF = int(1e9)

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# # graph = [[INF]*(n+1) for _ in range(n+1)]
# # for l in range(n+1):
# #     graph[l][l] = 0

# # for _ in range(m):
# #     start, end, cost = map(int, sys.stdin.readline().split())
# #     graph[start][end] = cost
# # print(graph)

# graph = [[0, 1000000000, 1000000000, 1000000000, 1000000000],
#          [1000000000, 0, 4, 1000000000, 6],
#          [1000000000, 3, 0, 7, 1000000000],
#          [1000000000, 5, 1000000000, 0, 4],
#          [1000000000, 1000000000, 1000000000, 2, 0]]

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         for k in range(1, n+1):
#             graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
# for l in graph[1:]:
#     print(l[1:])
