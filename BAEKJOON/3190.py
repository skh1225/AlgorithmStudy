import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
snake = deque([(1,1)])

dx, dy = [0,1,0,-1], [1,0,-1,0]

for _ in range(int(input())):
    r,c = map(int,input().split())
    graph[r][c] = 1


sec, d = 0,0
L = int(input())
for l in range(L+1):
    if l == L:
        S += N
    else:
        S, R = input().split()
        S = int(S)
    while sec < S:
        sec += 1
        hx, hy = snake[-1]
        nx, ny = hx+dx[d], hy+dy[d]
        if nx > 0 and ny > 0 and nx <= N and ny <= N:
            if graph[nx][ny] == 1:
                snake.append((nx,ny)); graph[nx][ny] = 0
            elif (nx,ny) in snake:
                break
            else:
                snake.popleft(); snake.append((nx,ny))
        else:
            break
    else:
        if R == 'D':
            d += 1
        else:
            d -= 1
        d %= 4
        continue
    break
print(sec)



