from collections import deque
def BFS(graph,v,visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        h = queue.popleft()
        print(h,end=' ')
        for i in graph[h]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False]*9
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
BFS(graph,1,visited)