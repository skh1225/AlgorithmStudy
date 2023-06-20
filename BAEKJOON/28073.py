import sys
from collections import deque

INF = int(1e6)+2
N, M = map(int, sys.stdin.readline().split())
S, E = sys.stdin.readline().split()
alpha = sys.stdin.readline().strip()
graph = [[] for _ in range(N+1)]
distance = [(INF,0) for _ in range(N+1)]
n_s, n_e = 0,0
for n in range(N):
    if alpha[n] == S:
        n_s = n+1
    if alpha[n] == E:
        n_e = n+1
    if n_s and n_e:
        break
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    if alpha[u-1] == S:
        u = n_s
    if alpha[v-1] == S:
        v = n_s
    if alpha[u-1] == E:
        u = n_e
    if alpha[v-1] == E:
        v = n_e
    if u == v:
        continue
    graph[u].append((u,v))
    graph[v].append((v,u))
    
if S == E:
    print(S)
else:
    queue = deque([[1,alpha[n_s-1], [n_s], 0]])
    distance[n_s] = (1, 0)
    breaker = False
    while queue and not breaker:
        q = queue.popleft()
        tmp = []
        for i in q[2]:
            tmp.extend(graph[i])
        tmp.sort(key=lambda x:alpha[x[1]-1])
        for T in tmp:
            if T[1] == n_s or distance[T[1]][0] != INF:
                continue
            if distance[T[1]][0] == INF:
                distance[T[1]] = (q[0]+1,T[0])
            if T[1] == n_e:
                answer = E
                for _ in range(q[0]):
                    n_e = distance[n_e][1]
                    answer = alpha[n_e-1]+ answer
                breaker = True
                break
            if queue and queue[-1][0] == q[0]+1 and queue[-1][1] == alpha[T[1]-1] and queue[-1][3] == tmp[0][1]:
                queue[-1][2].append(T[1])
            else:
                queue.append([q[0]+1, alpha[T[1]-1], [T[1]], tmp[0][1]])
    if breaker:
        print(answer)
    else:
        print('Aaak!')