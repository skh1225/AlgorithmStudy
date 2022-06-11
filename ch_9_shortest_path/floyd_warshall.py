import sys
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# graph = [[INF]*(n+1) for _ in range(n+1)]
# for l in range(n+1):
#     graph[l][l] = 0

# for _ in range(m):
#     start, end, cost = map(int, sys.stdin.readline().split())
#     graph[start][end] = cost
# print(graph)

graph = [[0, 1000000000, 1000000000, 1000000000, 1000000000],
         [1000000000, 0, 4, 1000000000, 6],
         [1000000000, 3, 0, 7, 1000000000],
         [1000000000, 5, 1000000000, 0, 4],
         [1000000000, 1000000000, 1000000000, 2, 0]]
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == i:
            continue
        for k in range(1, n+1):
            if k == i or k == j:
                continue
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

for a in range(1, n+1):
    print(' '.join(map(str, graph[a][1:])))
