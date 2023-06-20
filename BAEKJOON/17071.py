import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [[False, False] for _ in range(500001)] 
stack = [N]
visited[N][0] = True
answer = 0
while K <= 500000:
    if visited[K][answer%2]:
        break
    answer += 1
    K += answer
    tmp = []
    for s in stack:
        if s-1 >= 0 and not visited[s-1][answer%2]:
            visited[s-1][answer%2] = True
            tmp.append(s-1)
        if s+1 <= 500000 and not visited[s+1][answer%2]:
            visited[s+1][answer%2] = True
            tmp.append(s+1)
        if s*2 <= 500000 and not visited[s*2][answer%2]:
            visited[s*2][answer%2] = True
            tmp.append(s*2)
    stack = tmp

if K > 500000:
    print(-1)
else:
    print(answer)




