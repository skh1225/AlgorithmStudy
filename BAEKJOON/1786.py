import sys
input = sys.stdin.readline

T = input()[:-1]
P = input()[:-1]
n, m = len(T), len(P)
kmp, answer = [0 for _ in range(m)], []

j = 0
for i in range(1, m):
    if P[i] == P[j]:
        kmp[i] = j+1; j += 1
    else:
        while j > 0:
            j -= 1
            if P[i] == P[j]:
                for k in range(j):
                    if P[k] != P[i-j+k]:
                        break
                else:
                    kmp[i] = j+1; j += 1
                    break

s,num = 0,0
while s+m <= n:
    if P[num] == T[s+num]:
        num += 1
        if num == m:
            answer.append(s+1)
            s += m-kmp[m-1]; num = kmp[m-1]
    else:
        if num == 0:
            s += 1
        else:
            s += num-kmp[num-1]; num = kmp[num-1]
print(len(answer))
print(' '.join(map(str,answer)))

