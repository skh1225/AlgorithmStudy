import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int,input().split())
graph = [list(input().strip()) for _ in range(N)]
x1,y1,x2,y2 = map(int,input().split())
dx,dy = [0,0,1,-1], [1,-1,0,0]

def bfs(x1,y1):
    for i in range(4):
        nx,ny,cnt = x1+dx[i],y1+dy[i],1
        while cnt<=K and nx>0 and ny>0 and nx<=N and ny<=M and graph[nx-1][ny-1]!='#':
            if graph[nx-1][ny-1] != '.':
                if graph[nx-1][ny-1] > graph[x1-1][y1-1]:
                    nx += dx[i]; ny += dy[i]; cnt += 1
                    continue
                else:
                    break
            graph[nx-1][ny-1] = graph[x1-1][y1-1]+1
            if nx==x2 and ny==y2:
                return
            queue.append((nx,ny))
            nx += dx[i]; ny += dy[i]; cnt += 1
graph[x1-1][y1-1]=0
queue = deque([(x1,y1)])
while queue:
    x,y = queue.popleft()
    bfs(x,y)
    if graph[x2-1][y2-1] != '.':
        print(graph[x2-1][y2-1])
        break
else:
    print(-1)
