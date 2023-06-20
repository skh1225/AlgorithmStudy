V,E = 7,9
cost = [29,75,35,34,7,23,13,53,25]
edges = [(1,2),(1,5),(2,3),(2,6),(3,4),(4,6),(4,7),(5,6),(6,7)]
node = [i for i in range(V+1)]
graph = []
for i in range(E):
    graph.append((cost[i],edges[i][0],edges[i][1]))

graph.sort()
def find_node(node, x):
    if node[x] != x:
        node[x] = find_node(node,node[x])
    return node[x]

def union_node(node, graph, n):
    cnt = 0
    answer = 0
    for G in graph:
        cost, x, y = G
        x, y = find_node(node, x), find_node(node, y)
        if x > y:
            node[x] = y
        elif y > x:
            node[y] = x
        else:
            continue
        answer += cost
        cnt += 1
        if cnt == n-1:
            return answer
    return False

print(union_node(node, graph, V))