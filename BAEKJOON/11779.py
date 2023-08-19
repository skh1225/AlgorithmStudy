import sys
import heapq
input = sys.stdin.readline
INF = int(1e8)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    x,y,c = map(int,input().split())
    graph[x].append((y,c))
s,e = map(int,input().split())
distance = [INF for _ in range(n+1)]
prev = [0 for _ in range(n+1)]
heap = [(0,s)]; distance[s] = 0

while heap:
    c,x = heapq.heappop(heap)
    if x == e:
        cost = c
        break
    if c == distance[x]:
        for n_x,n_c in graph[x]:
            if distance[n_x] > c+n_c:
                distance[n_x] = c+n_c; prev[n_x] = x
                heapq.heappush(heap,(c+n_c,n_x))

stack = [e]
while stack[-1] != s:
    stack.append(prev[stack[-1]])
stack.reverse()
print(cost)
print(len(stack))
print(' '.join(map(str,stack)))
