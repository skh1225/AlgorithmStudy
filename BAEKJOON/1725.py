import sys
input = sys.stdin.readline

N = int(input())
graph = [int(input()) for _ in range(N)]
l_to_r, r_to_l = [0 for _ in range(N)], [N-1 for _ in range(N)]
tmp = []
for n in range(N):
    if not tmp:
        tmp.append(n)
    else:
        while tmp and graph[tmp[-1]] >= graph[n]:
            tmp.pop()
        if tmp:
            l_to_r[n] = tmp[-1]+1
        tmp.append(n)
    
tmp = []
for n in reversed(range(N)):
    if not tmp:
        tmp.append(n)
    else:
        while tmp and graph[tmp[-1]] >= graph[n]:
            tmp.pop()
        if tmp:
            r_to_l[n] = tmp[-1]-1
        tmp.append(n)

answer = 0
for n in range(N):
    answer = max(answer, (r_to_l[n]-l_to_r[n]+1)*graph[n])
print(answer)