import sys
N, M = map(int,sys.stdin.readline().split())
cnt = 0
while N != 1:
    if N//M == 0:
        cnt += N-1
        N = 1
    elif N%M == 0:
        cnt += 1
        N /= M
    else:
        cnt += N%M
        N -= N%M
print(cnt)