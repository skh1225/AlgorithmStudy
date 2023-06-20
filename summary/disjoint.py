V, M = 6, 4
union = [(2,4),(1,3),(3,4),(5,6)]
node = [i for i in range(V+1)]

def find_node(node, x):
    if node[x] != x:
        node[x] = find_node(node, node[x])
    return node[x]

def union_node(node, union):
    for u in union:
        a,b = u
        x,y = find_node(node,a), find_node(node,b)
        if x > y:
            node[x] = y
        else:
            node[y] = x

union_node(node,union)
print(node)
for i in range(1,V+1):
    find_node(node,i)
print(node)

