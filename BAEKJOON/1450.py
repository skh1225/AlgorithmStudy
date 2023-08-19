import sys
input = sys.stdin.readline
N, C = map(int, input().split())
W = list(map(int,input().split()))
W1 = W[:N//2]; W2 = W[N//2:]
sum1,sum2 = [C],[0]

for w1 in W1:
    for s1 in sum1[:]:
        if s1-w1 >= 0:
            sum1.append(s1-w1)
for w2 in W2:
    for s2 in sum2[:]:
        if s2+w2 <= C:
            sum2.append(s2+w2)
sum2.sort()
answer = 0
for s1 in sum1:
    start, end = 0, len(sum2)
    while start+1 < end:
        mid = (start+end)//2
        if s1 >= sum2[mid]:
            start = mid
        else:
            end = mid
    answer += end
print(answer)
