import sys
input = sys.stdin.readline

N, S, E, M = map(int, input().split())
edges = [list(map(int,input().split())) for _ in range(M)]
money = list(map(int, input().split()))
INF = int(1e6)*N

for edge in edges:
    edge[2] -= money[edge[1]]

dist = [INF for _ in range(N)]

def bf(start,end):
    dist[start] = 0
    result = money[start]
    cycle = []
    for n in range(N):
        for s,e,c in edges:
            if dist[s] < INF and dist[s]+c < dist[e]:
                dist[e] = dist[s]+c
                if n == N-1:
                    cycle.append(e)
        if n == N-2:
            if dist[end] == INF:
                return 'gg', False
            else:
                result -= dist[end]
    return result, cycle

def bfs(start,end):
    visited = [False for _ in range(N)]
    visited[start] = True
    for n in range(N):
        for s,e,_ in edges:
            if visited[s]:
                if e == end:
                    return True
                visited[e] = True
    return False

result, cycle = bf(S,E)

if cycle:
    for c in cycle:
        if bfs(c,E):
            print('Gee')
            break
    else:
        print(result)
else:
    print(result)


