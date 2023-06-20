import sys
input = sys.stdin.readline
INF = int(1e7)

def bf(start):
    dist[start] = 0
    for n in range(N):
        for s in range(1,N+1):
            for e,t in graph[s]:
                if dist[s]+t < dist[e]:
                    dist[e] = dist[s]+t
                    if n == N-1:
                        return 'YES'
    return 'NO'

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int,input().split())
        graph[S].append((E,T)); graph[E].append((S,T))
    for _ in range(W):
        S, E, T = map(int,input().split())
        graph[S].append((E,-T))
    
    dist = [INF for _ in range(N+1)]
    print(bf(1))