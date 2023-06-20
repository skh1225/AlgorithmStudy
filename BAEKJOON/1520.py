import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
dRow, dCol = [0,0,1,-1], [1,-1,0,0]

def dfs(x,y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    else:
        dp[x][y] = 0
        for i in range(4):
            n_x, n_y = x+dRow[i],y+dCol[i]
            if n_x >= 0 and n_y >= 0 and n_x < M and n_y < N:
                if graph[n_x][n_y] < graph[x][y]:
                    dp[x][y] += dfs(n_x,n_y)
    return dp[x][y]

print(dfs(0,0))


    