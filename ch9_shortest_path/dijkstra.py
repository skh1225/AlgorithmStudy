import sys
INF = int(1e9)

num_edge, num_vertex = map(int, sys.stdin.readline().split())
start_edge = int(sys.stdin.readline())

# graph = [[] for _ in range(num_edge+1)]
# for _ in range(num_vertex):
#     start, end, cost = map(int, sys.stdin.readline().split())
#     graph[start].append((end, cost))

graph = [[], [[2, 2], [3, 5], [4, 1]], [[3, 3], [4, 2]], [
    [2, 3], [6, 5]], [[3, 3], [5, 1]], [[3, 1], [6, 2]], []]


def get_short_edge(result, visited):
    edge, value = 0, INF
    for i in range(1, num_edge+1):
        if visited[i] == False and result[i] < value:
            value = result[i]
            edge = i
    if edge == 0:
        return False
    return edge


def dijkstra(start, graph, num_edge):
    result = [INF] * (num_edge+1)
    visited = [True]+[False] * (num_edge)
    edge = start
    result[edge] = 0
    while edge != 0:
        for j in graph[edge]:
            result[j[0]] = min(result[j[0]], result[edge]+j[1])
        visited[edge] = True
        edge = get_short_edge(result, visited)
    return result


print(dijkstra(start_edge, graph, num_edge))
