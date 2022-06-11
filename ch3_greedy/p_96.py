import sys
N,M = map(int, sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
tmp = []
for i in data:
    tmp.append(min(i))
print(max(tmp))