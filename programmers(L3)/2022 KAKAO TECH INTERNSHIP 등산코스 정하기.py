import heapq

def solution(n, paths, gates, summits):
    summits = set(summits)
    answer = []
    graph = [[] for _ in range(n+1)]
    for path in paths:
        graph[path[0]].append(path[1:])
        graph[path[1]].append([path[0],path[2]])
    for summit in summits:
        heap = [[0,summit]]
        visited = [False]*(n+1)
        while heap:
            intensity, node = heapq.heappop(heap)
            if answer and answer[0][0] < intensity:
                break
            if node in gates:
                heapq.heappush(answer,[intensity, summit])
                break
            visited[node] = True
            for num, i in graph[node]:
                if not visited[num] and not num in summits:
                    heapq.heappush(heap, [max(i,intensity), num])
    return [answer[0][1],answer[0][0]]