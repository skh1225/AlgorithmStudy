import sys

N = int(sys.stdin.readline())

d = [0]*(N+1)

for i in range(N+1):
    if i == 1 or i == 0:
        d[i] = 1
    else:
        d[i] = d[i-1] + d[i-2]*2
print(d[-1])