import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dRow, dCol = [1,-1,0,0], [0,0,1,-1]

def merge(graph,i):
    tmp = deepcopy(graph)
    if dRow[i] == -1:
        r_range = range(N-1,-1,-1)
    else:
        r_range = range(N)
    if dCol[i] == -1:
        c_range = range(N-1,-1,-1)
    else:
        c_range = range(N)
    for r in r_range:
        for c in c_range:
            if tmp[r][c] != 0:
                x,y = r,c
                while x+dRow[i] >=0 and y+dCol[i] >= 0 and x+dRow[i] < N and y+dCol[i] < N:
                    x += dRow[i]; y += dCol[i]
                    if tmp[x][y] == 0:
                        continue
                    else:
                        if tmp[x][y] == tmp[r][c]:
                            tmp[r][c] += tmp[x][y]
                            tmp[x][y] = 0
                        break
    for r in r_range:
        for c in c_range:
            if tmp[r][c] == 0:
                x,y = r,c
                while x+dRow[i] >=0 and y+dCol[i] >= 0 and x+dRow[i] < N and y+dCol[i] < N:
                    x += dRow[i]; y += dCol[i]
                    if tmp[x][y] != 0:
                        tmp[x][y], tmp[r][c] = tmp[r][c], tmp[x][y]
                        break
    return tmp

def dfs(graph, n):
    answer = 0
    if n == 5:
        for G in graph:
            answer = max(answer,max(G))
        return answer
    for i in range(4):
        answer = max(answer,dfs(merge(graph,i),n+1))
    return answer

print(dfs(graph,0))

