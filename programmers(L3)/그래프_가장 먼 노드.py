from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    visited[1] = 1
    queue = deque([1])
    while len(queue) > 0:
        removed = queue.popleft()
        for i in graph[removed]:
            if visited[i]:
                continue
            visited[i] = visited[:][removed] + 1
            queue.append(i)
    for i in visited:
        if i == max(visited):
            answer += 1
    return answer
