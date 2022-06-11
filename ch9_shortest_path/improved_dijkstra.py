import sys
import heapq

num_edge, num_vertex = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(num_edge+1)]

# for _ in range(num_vertex):
#     start, end, cost = map(int, sys.stdin.readline().split())
#     graph[start].append((end, cost))
# print(graph)

graph = [[], [[2, 2], [3, 5], [4, 1]], [[3, 3], [4, 2]], [
    [2, 3], [6, 5]], [[3, 3], [5, 1]], [[3, 1], [6, 2]], []]
INF = int(1e9)
distance = []
heapq.heapify(distance)
result = [INF]*(num_edge+1)
visited = [False]*(num_edge+1)
visited[0] = True


def dijkstra(start):
    heapq.heappush(distance, (0, start))
    while len(distance) > 0:
        c, i = heapq.heappop(distance)
        if visited[i] == False:
            visited[i] = True
            result[i] = c
            for j in graph[i]:
                heapq.heappush(distance, (j[1]+c, j[0]))
    print(result)p
dijkstra(1)
