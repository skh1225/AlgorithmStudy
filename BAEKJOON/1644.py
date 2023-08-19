import sys
input = sys.stdin.readline

N = int(input())
prime = []
is_prime = [False for _ in range(N+1)]
num = 2
while N >= num:
    if not is_prime[num]:
        prime.append(num)
        tmp = num*2
        while N >= tmp:
            is_prime[tmp] = True
            tmp += num
    num += 1

s,e = 0,0
S = 0
answer = 0
while True:
    if S <= N:
        if S == N:
            answer += 1
        if e == len(prime):
            break
        S += prime[e]
        e += 1
    else:
        S -= prime[s]
        s += 1
print(answer)

        
