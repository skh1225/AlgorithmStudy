import sys
input = sys.stdin.readline
 
N, M, H = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(H+1)]
answer = 4

for _ in range(M):
    x,y = map(int,input().split())
    graph[x][y] = 1

def check():
    for n in range(1,N):
        tmp = n
        for h in range(1,H+1):
            if graph[h][tmp]:
                tmp += 1
            elif graph[h][tmp-1]:
                tmp -= 1
        if tmp != n:
            return False
    return True

def dfs(cnt, x, y):
    global answer
    if cnt >= answer or cnt > 3:
        return
    if check():
        answer = min(answer,cnt)
        return
    for j in range(y,N):
        h = x if j == y else 1
        for i in range(h,H+1):
            if graph[i][j]==0 and graph[i][j-1]==0 and graph[i][j+1]==0:
                graph[i][j] = 1
                dfs(cnt+1,i+1,j)
                graph[i][j] = 0
dfs(0,1,1)
if answer > 3:
    print(-1)
else:
    print(answer)
    
                            


