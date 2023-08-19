import sys
input = sys.stdin.readline

N = int(input())
inOrder = list(map(int,input().split()))
postOrder = list(map(int,input().split()))
nodeOrder = [0 for _ in range(N+1)]
answer = []
for i in range(N):
    nodeOrder[inOrder[i]] = i

def solution(si,se,pi,pe):
    if si > se:
        return
    x = postOrder[pe]
    y = nodeOrder[x]
    answer.append(x)
    solution(si,y-1,pi,pi+y-1-si)
    solution(y+1,se,pe-se+y,pe-1)
solution(0,N-1,0,N-1)
print(' '.join(map(str,answer)))

