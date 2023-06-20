import sys

N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
p_s=0
answer = N+1

while end < N+1:
    if p_s < S:
        if end == N:
            break
        p_s += A[end]
        end += 1
    else:
        answer = min(answer, end-start)
        p_s -= A[start]
        start += 1

if answer == N+1:
    print(0)
else:
    print(answer)
