import heapq

A = []
heapq.heapify(A)
heapq.heappush(A, [1, 2])
print(len(A))
heapq.heappop(A)
print(len(A))
