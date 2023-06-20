import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = list(map(int,input().split()))
heapq.heapify(heap)
B, C = map(int, input().split())

answer = 0
limit = B
cnt = 1
while heap:
    A = heapq.heappop(heap)
    if A > limit:
        inc = (A-limit+C-1)//C
        cnt += inc; limit += C*inc
    answer += cnt
print(answer)
    