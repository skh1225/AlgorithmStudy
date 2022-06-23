def solution(stones, k):
    len_stones = len(stones)
    start = min(stones)
    end = max(stones)+1
    # stones의 모든 수가 1일때 1을 return
    if end-start == 1:
        return 1
    mid = (start+end)//2
    # binary_search
    while start+1 < end:
        if determinant(stones, len_stones, k, mid):
            start = mid
        else:
            end = mid
        mid = (start+end)//2
    return end


"""
stones : 징검다리
l : 징검다리의 길이
k : 건너뛸 수 있는 디딤돌의 최대 칸수
h : 몇 번째 사람인지
return : h번째 사람이 건널 수 있으면 True, 없으면 False
"""


def determinant(stones, l, k, h):
    for i in range(l):
        if i == 0:
            cnt = 0
        if stones[i] >= h:
            cnt = 0
        else:
            cnt += 1
        if cnt >= k:
            return False
    return True
