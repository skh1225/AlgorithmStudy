import sys
import heapq

N = int(sys.stdin.readline())

answer = N-1
curr = int(sys.stdin.readline())
heap = [[curr,1]]
for _ in range(N-1):
    curr = int(sys.stdin.readline())
    while heap and heap[0][0] < curr:
        _, C = heapq.heappop(heap)
        answer += C
    if not heap:
        answer -= 1
    if heap and heap[0][0] == curr:
        answer += heap[0][1]
        heap[0][1] += 1
        if len(heap) == 1:
            answer -= 1
    else:
        heapq.heappush(heap, [curr,1])

print(answer)