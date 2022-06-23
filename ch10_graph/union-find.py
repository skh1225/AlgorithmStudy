import sys

# 개선 전
# def find_parent(parent, x):
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

# 개선 후


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


v, e = map(int, sys.stdin.readline().split())
parent = [i for i in range(v+1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    union_parent(parent, a, b)
print('각 원소가 속한 집합:', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print('부모 테이블: '+' '.join(list(map(str, parent[1:]))))
