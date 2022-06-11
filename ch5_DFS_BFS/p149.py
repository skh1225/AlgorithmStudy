graph = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]

def DFS(m,n):
    len_m = len(graph)
    len_n = len(graph[0])
    if m < 0 or m > len_m-1 or n < 0 or n > len_n-1:
        return False
    if graph[m][n] == 0:
        graph[m][n] = 1
        DFS(m-1,n)
        DFS(m,n-1)
        DFS(m+1,n)
        DFS(m,n+1)
        return True
    return False


len_m = len(graph)
len_n = len(graph[0])
cnt = 0
for m in range(len_m):
    for n in range(len_n):
        if DFS(m,n) == True:
            cnt += 1
print(cnt)