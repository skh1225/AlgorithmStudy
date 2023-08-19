import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
prev = [[] for _ in range(int(1e4))]
cnt = 2
dx, dy = [0,0,1,-1], [1,-1,0,0]
def bfs(X,Y,cnt):
    queue = [(X,Y)]
    for x,y in queue:
        A = False
        for i in range(4):
            n_x,n_y = x+dx[i],y+dy[i]
            if n_x>=0 and n_y >=0 and n_x<N and n_y<N:
                if graph[n_x][n_y] == 1:
                    graph[n_x][n_y] = cnt
                    queue.append((n_x,n_y))
                if graph[n_x][n_y] == 0:
                    A = True
        if A:
            prev[cnt].append((x,y))
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            graph[x][y] = cnt
            bfs(x,y,cnt)
            cnt += 1
count =0
answer = 200
breaker = False
while True:
    for i in range(2,cnt):
        tmp = []
        for x,y in prev[i]:
            for j in range(4):
                n_x,n_y = x+dx[j],y+dy[j]
                if n_x>=0 and n_y >=0 and n_x<N and n_y<N:
                    if graph[n_x][n_y] == 0:
                        graph[n_x][n_y] = i
                        tmp.append((n_x,n_y))
                    elif graph[n_x][n_y] > i:
                        answer = min(answer,count)
                    elif graph[n_x][n_y] < i:
                        answer = min(answer,count+1)
        prev[i] = tmp
    if answer != 200:
        break
    count += 2
print(answer)


