import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def merge_sort(start, end):
    global answer
    if start < end:
        mid = (start+end)//2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        s1, s2, index = start, mid+1, start
        tmp = []
        while s1 <= mid and s2 <= end:
            if A[s1] <= A[s2]:
                tmp.append(A[s1])
                s1 += 1
            else:
                tmp.append(A[s2])
                answer += s2-index; s2 += 1
            index += 1
        if s2 > end:
            tmp += A[s1:mid+1]
        else:
            tmp += A[s2:end+1]
        for i in range(start, end+1):
            A[i] = tmp[i-start]

answer = 0
merge_sort(0, N-1)
print(answer)


