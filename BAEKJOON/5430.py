import sys

def solution(p,n,x):
    if n == 0:
        x = []
    else:
        x = x[1:-1].split(',')
    start, end = 0, len(x)
    cnt = 0
    for action in p:
        if action == 'R':
            cnt += 1
        else:
            if cnt%2 == 0:
                start += 1
            else:
                end -= 1
            if start > end:
                return 'error'
    if cnt%2 == 0:
        return '['+','.join(x[start:end])+']'
    else:
        return '['+','.join(reversed(x[start:end]))+']'

T = int(sys.stdin.readline())
answer = []
for _ in range(T):
    print(solution(sys.stdin.readline().strip(),int(sys.stdin.readline()),sys.stdin.readline().strip()))
