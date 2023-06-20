import sys
input = sys.stdin.readline

N = int(input())
k = int(input())
start, end = 1, N*N

if k == 1:
    print(1)
else:
    while start+1 < end:
        mid = (start+end)//2
        result = 0
        for n in range(1,N+1):
            result += min(N,mid//n)
        if result >= k:
            end = mid
        else:
            start = mid
    print(end)
