import sys
N = int(input())
K = list(map(int, sys.stdin.readline().split()))

d = [0]*(N+1)
for i in range(N+1):
    if i == 0:
        continue
    elif i == 1:
        d[i] = K[i-1]
        continue
    else:
        d[i] = max(d[i-1],d[i-2]+K[i-1])

print(d[-1])
