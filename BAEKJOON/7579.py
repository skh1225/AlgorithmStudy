import sys
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int,input().split())
memory = list(map(int,input().split()))
cost = list(map(int,input().split()))
dp = [0 for _ in range(10001)]

for n in range(N):
    end = 10000 - cost[n]
    for c in range(end,-1,-1):
        dp[c+cost[n]] = max(dp[c+cost[n]],dp[c]+memory[n])
answer = 0
while dp[answer] < M:
    answer += 1
print(answer)