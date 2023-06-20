import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int,input().split()))
stack = []
index = []
for i in A:
    if not stack:
        stack.append(i)
        index.append(0)
    elif stack[-1] < i:
        stack.append(i)
        index.append(len(stack)-1)
    else:
        start,end = 0,len(stack)-1
        if stack[0] >= i:
            stack[0] = i
            index.append(0)
        else:
            while start+1 < end:
                mid = (start+end)//2
                if stack[mid] > i:
                    end = mid
                elif stack[mid] < i:
                    start = mid
                else:
                    end = mid
                    break
            stack[end] = i
            index.append(end)
cnt = len(stack)-1
result = [0 for _ in range(cnt+1)]
for j in reversed(range(N)):
    if index[j] == cnt:
        result[cnt] = A[j]
        cnt -= 1
    if cnt < 0:
        break
print(len(stack))
print(' '.join(map(str,result)))