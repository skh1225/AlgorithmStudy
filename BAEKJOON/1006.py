import sys
input = sys.stdin.readline

def dynamic_programming(N,W,mode):
    dp = [[0 for _ in range(N+1)] for _ in range(3)]
    v0, v1 = graph[0][0], graph[1][0]
    for i in range(1,N+1):
        if i == 1:
            dp[0][1], dp[1][1] = 1, 1
            if mode%2 == 1:
                graph[0][0] = W
            if mode//2 == 1:
                graph[1][0] = W
            dp[2][1] = 1 if graph[0][0]+graph[1][0] <= W else 2
            continue
        b0 = 1 if graph[0][i-2]+graph[0][i-1] <= W else 2
        b1 = 1 if graph[1][i-2]+graph[1][i-1] <= W else 2
        b2 = 1 if graph[0][i-1]+graph[1][i-1] <= W else 2
        dp[0][i] = min(dp[1][i-1]+b0, dp[2][i-1]+1)
        dp[1][i] = min(dp[0][i-1]+b1, dp[2][i-1]+1)
        dp[2][i] = min(dp[2][i-1]+b2, dp[2][i-2]+b0+b1, dp[0][i]+1, dp[1][i]+1)
    if mode == 0:
        return dp[2][N]
    elif mode == 1:
        graph[0][0] = v0
        return dp[1][N]
    elif mode == 2:
        graph[1][0] = v1
        return dp[0][N]
    else:
        graph[0][0], graph[1][0] = v0, v1
        return dp[2][N-1]

num = int(input())
for _ in range(num):
    N, W = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(2)]
    if N <= 2:
        print(dynamic_programming(N,W,0))
    else:
        answer = dynamic_programming(N,W,0)
        A, B = graph[0][0]+graph[0][-1] <= W, graph[1][0]+graph[1][-1] <= W
        if A:
            answer = min(answer, dynamic_programming(N,W,1))
        if B:
            answer = min(answer, dynamic_programming(N,W,2))
        if A and B:
            answer = min(answer, dynamic_programming(N,W,3))
        print(answer)

