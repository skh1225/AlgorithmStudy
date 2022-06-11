from collections import deque
import sys

visited = [False]*9
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
         [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]


def BFS(start):
    queue = deque([start])
    visited[start] = True
    print(start)
    while len(queue) > 0:
        for i in graph[queue.popleft()]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i)


BFS(1)
