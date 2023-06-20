import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap1 = [-int(input())]
heap2 = []
print(-heap1[0])
for n in range(N-1):
    num = int(input())
    if n%2==0:
        if num < -heap1[0]:
            heapq.heappush(heap2,-heapq.heappushpop(heap1,-num))
        else:
            heapq.heappush(heap2,num)
    else:
        if num > heap2[0]:
            heapq.heappush(heap1,-heapq.heappushpop(heap2,num))
        else:
            heapq.heappush(heap1,-num)
    print(-heap1[0])
