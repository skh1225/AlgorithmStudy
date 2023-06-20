import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
SUM = sum(A)
half = SUM//2
dp = [0]+[-1 for _ in range(half)]
total = 0
for i in sorted(A):
    tmp = dp[:]; total += i
    if total <= half:
        search_range = total
    else:
        search_range = SUM-total
    for j in range(search_range+1):
        if j+i <= half and tmp[j+i] != -1:
            dp[j] = max(dp[j], tmp[j+i])
        if j-i >= 0:
            if tmp[j-i] != -1:
                dp[j] = max(dp[j], tmp[j-i]+i)
        elif i-j <= half:
            if tmp[i-j] != -1:
                dp[j] = max(dp[j], tmp[i-j]+j)
if dp[0] == 0:
    print(-1)
else:
    print(dp[0])