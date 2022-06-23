from collections import deque
from itertools import permutations


def solution(n, weak, dist):
    dist.sort(reverse=True)
    queue = deque([, 0]])
    while queue:
        i= queue.popleft()
        if len(i[0]) == 1:
            return i[1]+1
        if i[1] >= len(dist):
            break
        for idx, j in enumerate(i[0]):
            if dist[i[1]] >= n:
                return i[1]+1
            if dist[i[1]] + j >= n:
                tmp= binary_search(i[0], dist[i[1]] + j-n)
                if tmp+1 == idx:
                    return i[1]+1
                # ? = [start:idx],i[0]+1
                queue.append([i[0][tmp+1:idx], i[1]+1])
            else:
                tmp= binary_search(i[0], j+dist[i[1]])
                if idx == 0 and tmp == len(i[0]):
                    return i[1]+1
                # ? = [:idx]+[start:],i[0]+1
                queue.append([i[0][:idx]+i[0][min(tmp+1, len(i[0])):], i[1]+1])
    return -1


def binary_search(L, v):
    start= 0
    end= len(L)-1
    mid= (start+end)//2
    if L[start] > v:
        return start-1
    if L[end] < v:
        return end
    while start+1 < end:
        if L[mid] == v:
            return mid
        else:
            if L[mid] > v:
                end= mid
            else:
                start= mid
        mid= (start+end)//2
    if L[end] == v:
        return end
    return start
