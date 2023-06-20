import sys
import heapq

N, L = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
answer = [0 for _ in range(N)]
heap = []

cnt = 0
while cnt < N:
    heapq.heappush(heap,(A[cnt],cnt))
    while heap[0][1] <= cnt-L:
        heapq.heappop(heap)
    answer[cnt] = heap[0][0]
    cnt += 1

print(' '.join(map(str,answer)))