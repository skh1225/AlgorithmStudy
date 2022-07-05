def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for e in edges:
        graph[e[0]].append(e[1])
    answer = dfs(graph, info, 1, 0, graph[0])
    return answer

def dfs(graph, info, lamb, wolf, toGo):
    if lamb > wolf:
        result = lamb
        for i in toGo:
            tmp = toGo[:]
            tmp.remove(i)
            tmp.extend(graph[i])
            if info[i] == 0:
                result = max(result,dfs(graph, info, lamb+1, wolf, tmp))
            else:
                result = max(result,dfs(graph, info, lamb, wolf+1, tmp))
        return result
    return 0