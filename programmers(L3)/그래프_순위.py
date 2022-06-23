def dfs(start, n, graph):
    visited = [False]*(n+1)
    path = [start]
    visited[start] = True
    while len(path) > 0:
        for g in graph[path[-1]]:
            if visited[g]:
                continue
            else:
                visited[g] = True
                path.append(g)
                break
        else:
            path.pop()
    return sum(visited)-1


def solution(n, results):
    answer = 0
    graph_lower = [[] for _ in range(n+1)]
    graph_upper = [[] for _ in range(n+1)]
    for r in results:
        graph_lower[r[0]].append(r[1])
        graph_upper[r[1]].append(r[0])
    for i in range(1, n+1):
        if dfs(i, n, graph_upper)+dfs(i, n, graph_lower) == n-1:
            answer += 1
    return answer
