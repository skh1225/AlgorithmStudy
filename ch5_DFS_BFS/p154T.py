from collections import deque

m, n = map(int,input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int,input())))

def dfs(x,y):
    queue = deque()
    queue.append((x,y))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        x_,y_ = queue.popleft()
        for i in range(4):
            if x_+dx[i] > m-1 or x_+dx[i] < 0 or y_+dy[i] > n-1 or y_+dy[i] < 0:
                continue
            if graph[x_+dx[i]][y_+dy[i]] == 0:
                continue
            if graph[x_+dx[i]][y_+dy[i]] == 1:
                queue.append((x_+dx[i],y_+dy[i]))
                graph[x_+dx[i]][y_+dy[i]] = graph[x_][y_]+1
    return graph[m-1][n-1]

print(dfs(0,0))
