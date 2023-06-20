import sys
input = sys.stdin.readline

def solution(N,A):
    right = [N for _ in range(N)]
    left = [-1 for _ in range(N)]
    stack = []
    for i in range(N):
        if not stack:
            stack.append(i)
        else:
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
    stack = []
    for i in reversed(range(N)):
        if not stack:
            stack.append(i)
        else:
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
    return left, right

A = list(map(int,input().split()))

while A[0] != 0:
    N = A[0]
    A = A[1:]
    left, right = solution(N,A)
    answer = 0
    for i in range(N):
        answer = max(answer,(right[i]-left[i]-1)*A[i])
    print(answer)
    A = list(map(int,input().split()))
