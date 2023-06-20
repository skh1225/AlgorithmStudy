import sys 
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
heapq.heapify(gems)
bags.sort()
heap = []; answer = 0

for bag in bags:
    while gems and gems[0][0] <= bag:
        M, V = heapq.heappop(gems)
        heapq.heappush(heap,-V)
    if heap:
        answer -= heapq.heappop(heap)

print(answer)
        




