import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]

answer = 0
for n in range(N):
    value = 0
    for i in range(n):
        if A[i] < A[n]:
            value = max(value,dp[i])
    dp[n] = value+A[n]
    answer = max(answer,value+A[n])

print(answer)

            