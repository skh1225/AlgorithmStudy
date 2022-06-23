def solution(N, number):
    result = [[]] + [[int(str(N)*i)] for i in range(1, 9)]
    for i in range(1, 9):
        if int(str(N)*i) == number:
            return i
    for i in range(2, 9):  # N을 i 번 Search
        for j in range(1, i):  # j번 i-j번 Search
            for k in result[j]:
                for l in result[i-j]:
                    if k+l != 0:
                        result[i].append(k+l)
                    if k-l != 0:
                        result[i].append(k-l)
                    if k*l != 0:
                        result[i].append(k*l)
                    if k//l != 0:
                        result[i].append(k//l)
                    if k+l == number or k-l == number or k*l == number or k//l == number:
                        return i
    return -1
