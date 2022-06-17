def solution(key, lock):
    answer0 = True
    M = len(key)
    N = len(lock)
    Key = []
    Lock = []
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                Key.append((i, j))
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                Lock.append((i, j))
    if len(Lock) == 0:
        return True
    for rotate in range(4):
        for k in Key:
            visited = [False]*len(Lock)
            visited[0] = True
            x = Lock[0][0] - k[0]
            y = Lock[0][1] - k[1]
            for k_ in Key:
                if k_[0]+x >= N or k_[1]+y >= N or k_[0]+x < 0 or k_[1]+y < 0:
                    continue
                for idx, L in enumerate(Lock):
                    if (k_[0]+x, k_[1]+y) == L:
                        visited[idx] = True
                        break
                else:
                    break
            else:
                if False in visited:
                    pass
                else:
                    return True
        # 회전
        for i in range(len(Key)):
            Key[i] = (Key[i][1], M-1-Key[i][0])

    return False
