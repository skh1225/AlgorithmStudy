from collections import deque


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    else:
        for i in range(len(words)):
            if target == words[i]:
                end = i+1
                break
    graph = [[] for _ in range(len(words)+1)]
    for widx, w in enumerate(words):
        cnt = 0
        for bidx, b in enumerate(begin):
            if b == w[bidx]:
                continue
            else:
                cnt += 1
                if cnt > 1:
                    break
        if cnt == 1:
            graph[0].append(widx+1)
            graph[widx+1].append(0)
    for i in range(len(words)):
        for j in range(i, len(words)):
            cnt = 0
            for bidx, b in enumerate(words[i]):
                if b == words[j][bidx]:
                    continue
                else:
                    cnt += 1
                    if cnt > 1:
                        break
            if cnt == 1:
                graph[i+1].append(j+1)
                graph[j+1].append(i+1)
    INF = 51
    visited = [INF]*(len(words)+1)
    visited[0] = 0
    queue = deque([0])
    while len(queue) > 0:
        removed = queue.popleft()
        for g in graph[removed]:
            if visited[g] != INF:
                continue
            visited[g] = visited[:][removed] + 1
            if g == end:
                return visited[g]
            queue.append(g)
    return 0
