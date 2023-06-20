import sys
input = sys.stdin.readline
import heapq

N = int(input())
nodes = [tuple(map(int,input().split()+[i])) for i in range(N)]
parents = [i for i in range(N)]
heap = []

nodes.sort(key=lambda x: x[0])
for i in range(N-1):
    heapq.heappush(heap,(nodes[i+1][0]-nodes[i][0],nodes[i+1][3],nodes[i][3]))
nodes.sort(key=lambda x: x[1])
for i in range(N-1):
    heapq.heappush(heap,(nodes[i+1][1]-nodes[i][1],nodes[i+1][3],nodes[i][3]))
nodes.sort(key=lambda x: x[2])
for i in range(N-1):
    heapq.heappush(heap,(nodes[i+1][2]-nodes[i][2],nodes[i+1][3],nodes[i][3]))

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a, b = find(a), find(b)
    if a == b:
        return False
    else:
        if a > b:
            parents[a] = b
        else:
            parents[b] = a
    return True

cnt = 0
answer = 0
while cnt < N-1:
    cost, j, i = heapq.heappop(heap)
    if union(j,i):
        answer += cost
        cnt += 1
print(answer)
