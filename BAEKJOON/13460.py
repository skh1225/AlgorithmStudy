import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
dRow, dCol = [-1,1,0,0], [0,0,-1,1]

for n in range(N):
    for m in range(M):
        if graph[n][m] == 'R':
            r1, c1 = n, m
        if graph[n][m] == 'B':
            r2, c2 = n, m
queue = deque([(r1,c1,r2,c2,1)])
visited[r1][c1][r2][c2] = True

def move(x,y,dx,dy):
    cnt = 0
    while graph[x+dx][y+dy] != '#':
        x += dx; y += dy; cnt += 1
        if graph[x][y] == 'O':
            break
    return x, y, cnt

def bfs():
    while queue:
        r1,c1,r2,c2,t = queue.popleft()
        for i in range(4):
            x1,y1,cnt1 = move(r1,c1,dRow[i],dCol[i])
            x2,y2,cnt2 = move(r2,c2,dRow[i],dCol[i])
            if graph[x2][y2] == 'O':
                continue
            if graph[x1][y1] == 'O':
                return t
            if x1==x2 and y1==y2:
                if cnt1 > cnt2:
                    x1,y1 = x1-dRow[i],y1-dCol[i]
                else:
                    x2,y2 = x2-dRow[i],y2-dCol[i]
            if not visited[x1][y1][x2][y2] and t < 10:
                queue.append((x1,y1,x2,y2,t+1))
                visited[x1][y1][x2][y2] = True
    return -1

print(bfs())