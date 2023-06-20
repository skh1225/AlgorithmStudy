import sys

M, N = map(int,sys.stdin.readline().split())
dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
things = []
for m in range(1,M+1):
    weight, value = map(int, sys.stdin.readline().split())
    for n in range(N+1):
        if weight > n:
            dp[m][n] = dp[m-1][n]
        else:
            dp[m][n] = max(dp[m-1][n],dp[m-1][n-weight]+value)

print(dp[M][N])