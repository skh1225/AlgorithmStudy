# improved
import sys
import heapq
INF = int(1e9)

num_edge, num_vertex = map(int, sys.stdin.readline().split())
start_edge = int(sys.stdin.readline())
visited = [False]*(num_edge+1)
visited[0] = True
distance = [INF]*(num_edge+1)
# graph = [[] for _ in range(num_edge+1)]
# for _ in range(num_vertex):
#     start, end, cost = map(int, sys.stdin.readline().split())
#     graph[start].append((end, cost))

graph = [[], [[2, 2], [3, 5], [4, 1]], [[3, 3], [4, 2]], [
    [2, 3], [6, 5]], [[3, 3], [5, 1]], [[3, 1], [6, 2]], []]


def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    while len(heap) > 0:
        smallest = heapq.heappop(heap)
        if visited[smallest[1]]:
            continue
        visited[smallest[1]] = True
        distance[smallest[1]] = smallest[0]
        for i in graph[smallest[1]]:
            heapq.heappush(heap, [distance[smallest[1]]+i[1], i[0]])
    print(distance[1:])


dijkstra(1)
# normal
# import sys
# INF = int(1e9)

# num_edge, num_vertex = map(int, sys.stdin.readline().split())
# start_edge = int(sys.stdin.readline())
# visited = [False]*(num_edge+1)
# visited[0] = True
# distance = [INF]*(num_edge+1)
# # graph = [[] for _ in range(num_edge+1)]
# # for _ in range(num_vertex):
# #     start, end, cost = map(int, sys.stdin.readline().split())
# #     graph[start].append((end, cost))

# graph = [[], [[2, 2], [3, 5], [4, 1]], [[3, 3], [4, 2]], [
#     [2, 3], [6, 5]], [[3, 3], [5, 1]], [[3, 1], [6, 2]], []]


# def get_smallest():
#     smallest = 0
#     for i in range(1, num_edge+1):
#         if distance[i] < distance[smallest] and not visited[i]:
#             smallest = i
#     if smallest == 0:
#         return False
#     return smallest


# def dijkstra(start):
#     distance[start] = 0
#     smallest = start
#     while smallest:
#         visited[smallest] = True
#         for i in graph[smallest]:
#             distance[i[0]] = min(distance[i[0]], distance[smallest]+i[1])
#         smallest = get_smallest()
#     print(distance[1:])
# dijkstra(1)
