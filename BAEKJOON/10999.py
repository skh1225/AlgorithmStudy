import sys
input = sys.stdin.readline
from math import ceil, log2

N, M, K = map(int, input().split())
tree = [[0,0] for _ in range(2**ceil(log2(N)+1))]

def update(i,v,N=N):
    start, end = 0, N-1
    index = 1
    while start <= end:
        mid = (start+end)//2
        tree[index][0] += v
        if start == end:
            break
        if i <= mid:
            index *=2
            end = mid
        else:
            index = index*2+1
            start = mid+1

def segment_sum(a,z,index,start,end):
    if a > end or z < start:
        return 0
    if tree[index][1] != 0:
        tree[index][0] += (end-start+1)*tree[index][1]
        if index*2 < len(tree):
            tree[index*2][1] += tree[index][1]
            tree[index*2+1][1] += tree[index][1]
        tree[index][1] = 0
    s = 0
    mid = (start+end)//2
    if start >= a and end <= z:
        return tree[index][0]
    if z <= mid:
        s += segment_sum(a,z,index*2,start,mid)
    elif a > mid:
        s += segment_sum(a,z,index*2+1,mid+1,end)
    else:
        s += segment_sum(a,mid,index*2,start,mid)
        s += segment_sum(mid+1,z,index*2+1,mid+1,end)
    return s

def lazy_update(a,z,v,index,start,end):
    if a > end or z < start:
        return
    mid = (start+end)//2
    if start >= a and end <= z:
        tree[index][1] += v
        return
    if a<=end and a>=start and z<=end and z>=start:
        tree[index][0] += v*(z-a+1)
    elif a<=end and a>=start:
        tree[index][0] += v*(end-a+1)
    elif z<=end and z>=start:
        tree[index][0] += v*(z-start+1)
    if z <= mid:
        lazy_update(a,z,v,index*2,start,mid)
    elif a > mid:
        lazy_update(a,z,v,index*2+1,mid+1,end)
    else:
        lazy_update(a,mid,v,index*2,start,mid)
        lazy_update(mid+1,z,v,index*2+1,mid+1,end)

for i in range(N):
    update(i,int(input()))

Answer = []
for _ in range(K+M):
    command = tuple(map(int, input().split()))
    if command[0] == 1:
        lazy_update(command[1],command[2],command[3],1,1,N)
    else:
        Answer.append(segment_sum(command[1],command[2],1,1,N))

for A in Answer:
    print(A)

