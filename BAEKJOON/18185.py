import sys
input = sys.stdin.readline

N = int(input())
ramen = list(map(int,input().split()))
answer = sum(ramen)*2
i = 0
while i < N:
    if ramen[i] == 0:
        i += 1
        continue
    if i < N-2 and ramen[i+1] > ramen[i+2]:
        r = min(ramen[i],ramen[i+1],ramen[i+1]-ramen[i+2])
        ramen[i] -= r
        ramen[i+1] -= r
        answer += r
    else:
        r = ramen[i]
        for j in range(1,3):
            if i+j == N or ramen[i+j] == 0:
                break
            r = min(r,ramen[i+j])
        for j in range(3):
            if i+j == N or ramen[i+j] == 0:
                break
            ramen[i+j] -= r
        answer += r
print(answer)

    

    

