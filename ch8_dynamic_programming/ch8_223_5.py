import sys

N, M = map(int, sys.stdin.readline().split())
C = [int(sys.stdin.readline()) for _ in range(N)]

d = [-1]*(10001)

for j in C:
    d[j] = 1

for i in range(M):
    if i == 0:
        for j in C:
            d[j] = 1
    else:
        if d[i] == -1:
            continue
        else:
            for j in C:
                if i+j < 10001:
                    if d[i+j] == -1:
                        d[i+j] = d[i]+1
                    else:
                        d[i+j] = min(d[i+j],d[i]+1)
        +
print(d[M])