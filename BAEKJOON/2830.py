import sys
input = sys.stdin.readline
binary = [0]*20
N = int(input())
for _ in range(N):
    x = int(input())
    cnt = 0
    while x > 0:
        binary[cnt] += x%2
        x //= 2; cnt += 1
answer = 0
for i in range(20):
    answer += 2**i*binary[i]*(N-binary[i])
print(answer)