import sys

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
distance = [INF]*(num_edge+1)
visited = [False]*(num_edge+1)
visited[0] = True


def get_shortest():
    cost, index = INF, 0
    for idx, v in enumerate(visited):
        if v == False and cost > distance[idx]:
            cost, index = distance[idx], idx
    if index == 0:
        return False
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i, c in graph[start]:
        distance[i] = min(distance[i], distance[start]+c)
    shortest = get_shortest()
    while shortest:
        visited[shortest] = True
        for i, c in graph[shortest]:
            distance[i] = min(distance[i], distance[shortest]+c)
        shortest = get_shortest()
    print(distance)


dijkstra(1)
