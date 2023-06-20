import sys
N, K = map(int, sys.stdin.readline().split())

if N > K:
    print(N-K)
else:
    dp = [0 for _ in range(K+1)]
    for i in range(N):
        dp[i] = N-i
    for j in range(N+1,K+1):
        if j%2==0:
            dp[j] = min(dp[j//2],dp[j-1]+1)
        else:
            dp[j] = min(dp[(j+1)//2]+1,dp[j-1]+1)
    print(dp[K])