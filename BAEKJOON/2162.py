import sys
input = sys.stdin.readline

N = int(input())
V = [tuple(map(int,input().split())) for _ in range(N)]
P = [i for i in range(N)] 
R = []

def check(V1, V2):
    x1, y1, x2, y2 = V1
    x3, y3, x4, y4 = V2
    z = (x2-x1)*(y4-y3)-(x4-x3)*(y2-y1)
    if z == 0:
        if (x1-x3)*(y2-y3)-(x2-x3)*(y1-y3) == 0:
            X = (x1-x3)*(x2-x3) <= 0 or (x1-x4)*(x2-x4) <= 0 or (x3-x1)*(x4-x1) <= 0
            Y = (y1-y3)*(y2-y3) <= 0 or (y1-y4)*(y2-y4) <= 0 or (y3-y1)*(y4-y1) <= 0
            if X and Y:
                return True
        return False
    else:
        a = ((y4-y3)*(x3-x1)-(x4-x3)*(y3-y1))/z
        b = ((x2-x1)*(y1-y3)-(y2-y1)*(x1-x3))/z
        if a>=0 and a<=1 and b>=0 and b<=1:
            return True
    return False

for i in range(N-1):
    for j in range(i+1, N):
        if check(V[i],V[j]):
            R.append((i,j))

def find_parent(x):
    if P[x] != x:
        P[x] = find_parent(P[x])
    return P[x]

def union(x1,x2):
    p1, p2 = find_parent(x1), find_parent(x2)
    if p1 < p2:
        P[p2] = p1
    elif p1 > p2:
        P[p1] = p2

for r in R:
    x1, x2 = r
    union(x1,x2)

for i in range(N):
    find_parent(i)

answer_dic = {}
answer = 0

for p in P:
    answer_dic[p] = answer_dic.get(p,0)+1
    answer = max(answer, answer_dic[p])

print(len(answer_dic))
print(answer)

    
