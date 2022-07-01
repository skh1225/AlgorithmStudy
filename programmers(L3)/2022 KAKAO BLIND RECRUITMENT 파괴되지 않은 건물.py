def solution(board, skill):
    answer = 0
    M = len(board)
    N = len(board[0])
    cum = [[0]*N for _ in range(N)]
    for s in skill:
        if s[0] == 1:
            cum[s[1]][s[2]] -= s[5]
            if s[3] < M-1 and s[4] < N-1:
                cum[s[3]+1][s[2]] += s[5]
                cum[s[1]][s[4]+1] += s[5]
                cum[s[3]+1][s[4]+1] -= s[5]
            elif s[3] < M-1:
                cum[s[3]+1][s[2]] += s[5]
            elif s[4] < N-1:
                cum[s[1]][s[4]+1] += s[5]
        else:
            cum[s[1]][s[2]] += s[5]
            if s[3] < M-1 and s[4] < N-1:
                cum[s[3]+1][s[2]] -= s[5]
                cum[s[1]][s[4]+1] -= s[5]
                cum[s[3]+1][s[4]+1] += s[5]
            elif s[3] < M-1:
                cum[s[3]+1][s[2]] -= s[5]
            elif s[4] < N-1:
                cum[s[1]][s[4]+1] -= s[5]
    for x in range(N):
        for y in range(1, M):
            cum[y][x] += cum[y-1][x]
    for y in range(M):
        for x in range(1, N):
            cum[y][x] += cum[y][x-1]
    for x in range(N):
        for y in range(M):
            if cum[y][x] + board[y][x] > 0:
                answer += 1
    return answer
