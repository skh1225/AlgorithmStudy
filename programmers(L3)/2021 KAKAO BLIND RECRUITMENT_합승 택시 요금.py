import heapq


def dijkstra(start, end, n, graph):
    INF = int(1e9)
    visited = [False]*(n+1)
    cost = [INF]*(n+1)
    cost[start] = 0
    heap = [[cost[start], start]]
    while len(heap) > 0:
        C = heapq.heappop(heap)
        if visited[C[1]]:
            continue
        visited[C[1]] = True
        if C[1] == end:
            return C[0]
        for g in graph[C[1]]:
            cost[g[0]] = min(cost[g[0]], C[0]+g[1])
            heapq.heappush(heap, [cost[g[0]], g[0]])
    if end:
        return INF
    else:
        return cost


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    INF = int(1e9)
    result = INF
    for f in fares:
        graph[f[0]].append((f[1], f[2]))
        graph[f[1]].append((f[0], f[2]))
    cost = dijkstra(s, False, n, graph)
    for i in range(1, n+1):
        result = min(result, cost[i]+dijkstra(i, a,
                     n, graph)+dijkstra(i, b, n, graph))
    return result
