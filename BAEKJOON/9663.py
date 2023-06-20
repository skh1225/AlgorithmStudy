import sys
N = int(sys.stdin.readline())

def N_Queen(stack, r, N):
    answer = 0
    visited = [False for _ in range(N)]
    if r==N:
        return 1
    for i in range(r):
        visited[stack[i]] = True
        if stack[i]-(r-i) >= 0:
            visited[stack[i]-(r-i)] = True
        if stack[i]+(r-i) < N:
            visited[stack[i]+(r-i)] = True
    for i in range(N):
        if not visited[i]:
            stack[r]=i
            answer += N_Queen(stack,r+1,N)
    return answer
            
stack = [0 for _ in range(N)]
print(N_Queen(stack,0,N))