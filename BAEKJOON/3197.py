import sys
import copy
from collections import deque
input = sys.stdin.readline

R, C = map(int,input().split())
graph, L, prev_p, next_l = [], [], [], []
dRow, dCol = [0,0,-1,1], [1,-1,0,0]

for r in range(R):
    graph.append(list(input().strip()))

for r in range(R):
    for c in range(C):
        if graph[r][c] == 'L':
            L.append((r,c))
            graph[r][c] = '.'
        if graph[r][c] == '.':
            for i in range(4):
                n_r, n_c = r+dRow[i], c+dCol[i]
                if n_r >= 0 and n_c >= 0 and n_r < R and n_c < C and graph[n_r][n_c] == 'X':
                    prev_p.append((r,c))
                    break

def bfs(graph, R, C, next_l):
    tmp_l = []
    for r,c in next_l:
        if graph[r][c] == 'L':
            continue
        queue = deque([(r,c)])
        graph[r][c] = 'L'
        while queue:
            t_r,t_c = queue.popleft()
            for i in range(4):
                n_r, n_c = t_r+dRow[i], t_c+dCol[i]
                if n_r >= 0 and n_c >= 0 and n_r < R and n_c < C:
                    if graph[n_r][n_c] == '.':
                        graph[n_r][n_c] = 'L'
                        queue.append((n_r,n_c))
                    if graph[n_r][n_c] == 'X':
                        tmp_l.append((n_r,n_c))
    return tmp_l

def next_day(graph, prev_p):
    tmp_p = []
    for r, c in prev_p:
        for i in range(4):
            n_r, n_c = r+dRow[i], c+dCol[i]
            if n_r >= 0 and n_c >= 0 and n_r < R and n_c < C:
                if graph[n_r][n_c] == 'X':
                    graph[n_r][n_c] = '.'
                    tmp_p.append((n_r,n_c))
    return tmp_p

def check():
    for l_r,l_c in L:
        if graph[l_r][l_c] != 'L':
            break
    else:
        return False
    return True

answer = 0
next_l.append(L[0])
next_l = bfs(graph, R, C, next_l)

while check():
    prev_p = next_day(graph, prev_p)
    next_l = bfs(graph, R, C, next_l)
    answer += 1

print(answer)