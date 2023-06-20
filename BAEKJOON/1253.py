import sys

def binary_search(A,x):
    start = 0
    end = len(A)-1
    answer = -1
    if A[start] > x or A[end] < x:
        return -1
    while start+1 < end:
        mid = (start+end)//2
        if A[mid] > x:
            end = mid
        elif A[mid] < x:
            start = mid
        else:
            return mid
    if A[start] == x:
        return start
    elif A[end] == x:
        return end
    else:
        return -1

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

A_dict = dict()
for a in A:
    A_dict[a] = A_dict.get(a,0)+1
A = sorted(list(set(A)))
visited=[False for _ in range(len(A))]

for i in range(len(A)):
    for j in range(i,len(A)):
        if i==j and A_dict[A[i]] < 2:
            continue
        result = binary_search(A,A[i]+A[j])
        if i==result and A_dict[A[i]] < 2:
            continue
        elif j==result and A_dict[A[j]] < 2:
            continue
        elif i==j and j==result and A_dict[A[i]] < 3:
            continue
        if result > -1:
            visited[result] = True

answer = 0
for i in range(len(A)):
    if visited[i]:
        answer += A_dict[A[i]]
print(answer)