import sys
input = sys.stdin.readline

def update(I,V):
    prev = segment_sum(I,I)
    while I <= N:
        T[I] += V-prev
        I += (I & -I)

def prefix_sum(I):
    result = 0
    while I > 0:
        result += T[I]
        I -= (I & -I)
    return result

def segment_sum(S,E):
    return prefix_sum(E) - prefix_sum(S-1)

N, M, K = map(int, input().split())
T = [0 for _ in range(N+1)]

for n in range(N):
    update(n+1, int(input()))

for _ in range(M+K):
    a,b,c = map(int, input().split())
    if a == 1:
        update(b,c)
    else:
        print(segment_sum(b,c))


