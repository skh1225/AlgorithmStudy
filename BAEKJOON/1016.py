import sys
import math

m, n = map(int, sys.stdin.readline().split())
M, N = 2, max(2, int(math.sqrt(n)))
det = [True]*(n-m+1)

for i in range(M, N+1):
    mul = m//(i*i)
    while i*i*mul <= n:
        if i*i*mul >= m:
            det[i*i*mul-m] = False
        mul += 1

print(sum(det))
