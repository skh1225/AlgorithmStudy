import sys

V, E = map(int,sys.stdin.readline().split())
edges = []
parents = [i for i in range(V+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b))
edges.sort()

def find_parents(parents, a):
    if parents[a] != a:
        parents[a] = find_parents(parents,parents[a])
    return parents[a]

def union_parents(parents, a, b):
    a,b = find_parents(parents,a), find_parents(parents,b)
    if a > b:
        parents[a] = b
    elif b > a:
        parents[b] = a
    else:
        return False
    return True

answer = 0
cnt = 0
for edge in edges:
    c, a, b = edge
    if union_parents(parents, a, b):
        answer += c
        cnt += 1

if cnt == V-1:
    print(answer)