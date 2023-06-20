import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
answer = ['-1' for _ in range(N)]

stack = [A[-1]]
for i in reversed(range(N-1)):
    while stack:
        if stack[-1] > A[i]:
            answer[i] = str(stack[-1])
            stack.append(A[i])
            break
        else:
            stack.pop()
    if not stack:
        stack.append(A[i])
print(' '.join(answer))