import sys

M, N = map(int,sys.stdin.readline().split())
graph = []
s = set()
cnt = 0
for n in range(N):
    value = list(map(int,sys.stdin.readline().split()))
    graph.append(value)
    for m in range(M):
        if value[m] == 1:
            s.add((n,m))
        elif value[m] == 0:
            cnt += 1
answer = 0
while s:
    if cnt == 0:
        break
    tmp = set()
    dRow, dCol = [0,0,1,-1], [1,-1,0,0]
    for i in s:
        n,m = i
        for j in range(4):
            next_n, next_m = n+dRow[j], m+dCol[j]
            if next_n >= 0 and next_m >= 0 and next_n < N and next_m < M:
                if graph[next_n][next_m] == 0:
                    tmp.add((next_n,next_m))
                    graph[next_n][next_m] = 1
    s = tmp
    cnt -= len(s)
    answer += 1
if cnt == 0:
    print(answer)
else:
    print(-1)