import heapq


def solution(board):
    answer = 0
    heap = [[0, 0, 0, '0'], [0, 0, 0, '2']]
    n = len(board)
    visited = [[[False]*n for _ in range(n)] for _ in range(4)]
    direction = {'0': [0, 1], '1': [0, -1], '2': [1, 0], '3': [-1, 0]}
    while heap[0][1:3] != [n-1, n-1]:
        removed = heapq.heappop(heap)
        if visited[int(removed[3])][removed[1]][removed[2]]:
            continue
        else:
            visited[int(removed[3])][removed[1]][removed[2]] = True
        for d in direction:
            x = removed[1]+direction[d][0]
            y = removed[2]+direction[d][1]
            if x < 0 or x > n-1 or y < 0 or y > n-1 or board[x][y] == 1:
                continue
            if d == removed[-1]:
                cost = removed[0] + 100
            else:
                cost = removed[0] + 600
            heapq.heappush(heap, [cost, x, y, d])
    return heap[0][0]
