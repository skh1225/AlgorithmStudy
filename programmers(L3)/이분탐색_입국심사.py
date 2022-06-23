import heapq


def solution(n, times):
    answer = 0
    start = 0
    end = min(times)*n
    while start < end:
        sum = n
        judge = False
        mid = (start+end)//2
        for t in times:
            sum -= mid//t
            if sum <= 0:
                judge = True
                break
        if judge:
            end = mid
        else:
            start = mid+1
    return end
