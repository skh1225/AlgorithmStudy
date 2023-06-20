from collections import deque

V,E = 7,8
start = [1,1,2,2,3,4,5,6]
end = [2,5,3,6,4,7,6,4]
indegree = [0 for _ in range(V+1)]
graph = [[] for _ in range(V+1)]
queue = deque([])
for i in range(E):
    graph[start[i]].append(end[i])
    indegree[end[i]] += 1

for i in range(1,V+1):
    if not indegree[i]:
        queue.append(i)

while queue:
    node = queue.popleft()
    print(node)
    for G in graph[node]:
        indegree[G] -= 1
        if not indegree[G]:
            queue.append(G)
