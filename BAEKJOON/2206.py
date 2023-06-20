import sys
import heapq

R, C = map(int,sys.stdin.readline().split())
graph = []
for _ in range(R):
    graph.append(list(map(int,sys.stdin.readline().strip())))
INF = int(1e6)

d0 = [[INF for _ in range(C)] for _ in range(R)]
d1 = [[INF for _ in range(C)] for _ in range(R)]

heap = [(1,1,0,0)]
dRow, dCol = [0,0,1,-1], [1,-1,0,0]
answer = -1
while heap:
    cost, broke, r, c = heapq.heappop(heap)
    if r == R-1 and c == C-1:
        answer = cost
        break
    for i in range(4):
        n_r,n_c = r+dRow[i], c+dCol[i]
        if n_r >= 0 and n_c >= 0 and n_r < R and n_c < C:
            if broke-graph[n_r][n_c] < 0:
                continue
            elif broke-graph[n_r][n_c] == 0:
                if d0[n_r][n_c] > cost+1:
                    d0[n_r][n_c] = cost+1
                    heapq.heappush(heap, (cost+1,0,n_r,n_c))
            else:
                if d1[n_r][n_c] > cost+1:
                    d1[n_r][n_c] = cost+1
                    heapq.heappush(heap, (cost+1,1,n_r,n_c))
print(answer)