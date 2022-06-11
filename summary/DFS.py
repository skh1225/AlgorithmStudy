# 예제
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline()[:-1])) for _ in range(n)]


def dfs(x, y):
    print(x, y)
    if x < 0 or y < 0 or x > n-1 or y > m-1 or graph[x][y] == 1:
        return False
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True


cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1
print(cnt)


# 기본 구현
# visited = [False]*9
# graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
#          [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]


# def DFS(start):
#     tmp = []
#     tmp.append(start)
#     visited[start] = True
#     print(start)
#     while len(tmp) > 0:
#         for i in graph[tmp[-1]]:
#             if not visited[i]:
#                 tmp.append(i)
#                 visited[i] = True
#                 print(i)
#                 break
#         else:
#             tmp.pop()
# DFS(1)
