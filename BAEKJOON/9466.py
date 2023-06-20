import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    visited = [[False,0] for _ in range(N+1)]
    S = [0]+list(map(int,input().split()))
    answer = 0
    for start in range(1,N+1):
        curr,cnt = start,0
        if visited[curr][0]:
            continue
        visited[curr][0] = start
        while not visited[S[curr]][0]:
            cnt += 1
            curr = S[curr]
            visited[curr][0] = start
            visited[curr][1] = cnt
        if visited[S[curr]][0] == start:
            answer += visited[S[curr]][1]
        else:
            answer += visited[curr][1]+1
    print(answer)