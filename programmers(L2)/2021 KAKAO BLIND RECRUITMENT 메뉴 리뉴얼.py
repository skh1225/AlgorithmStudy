from itertools import combinations


def solution(orders, course):
    answer = []
    sorted_orders = []
    for order in orders:
        sorted_orders.append(sorted(order))

    for c in course:
        tmp_c = []
        breaker = False
        for order in sorted_orders:
            tmp_c.append(set(combinations(order, c)))
        for i in range(len(orders), 1, -1):  # 최대 코스부터
            for combination in combinations(range(len(orders)), i):  # i 개 코스
                tmp = None
                for com in combination:
                    if tmp == None:
                        tmp = tmp_c[com]
                    else:
                        tmp = tmp & tmp_c[com]
                    if tmp == set():
                        break
                else:
                    for t in tmp:
                        answer.append(''.join(t))
                    breaker = True
            if breaker:
                break
    return sorted(answer)