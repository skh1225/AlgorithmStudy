import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ARR = list(map(int,input().split()))
R = [0 for _ in range(M)]
tmp = 0

for n in range(N):
    tmp = (tmp+ARR[n])%M
    R[tmp] += 1

answer = R[0]
for m in range(M):
    answer += (R[m]-1)*R[m]//2

print(answer)

