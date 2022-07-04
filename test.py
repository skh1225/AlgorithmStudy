from itertools import combinations


def solution(n, info):
    answer = [0 for _ in range(11)]
    result = []
    for i in range(n):
        combination = combinations(range(10), i)
        for com in combination:
            cnt = 0
            for c in com:
                cnt += info[c]+1
                if cnt > n:
                    break
            else:
                Apache = 0
                tmp = sorted(list(com), reverse=True)
                for j in range(10):
                    if j not in tmp and info[j] > 0:
                        Apache += 10-j
                if len(tmp)*10-sum(tmp) > Apache:
                    remains = n-cnt
                    result.append([len(tmp)*10-sum(tmp), remains, tmp])
    result.sort()
    if result:
        print(result)
        for k in result[-1][2]:
            answer[k] = info[k]+1
        answer[-1] = result[-1][1]
        return answer
    else:
        return [-1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
