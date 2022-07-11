import math


def solution(fees, records):
    answer = []
    info = dict()
    for record in records:
        t1, number, IO = record.split()
        if IO == 'IN':
            info[number] = info.get(number, ['', 0])
            info[number][0] = t1
        elif IO == 'OUT':
            t0, info[number][0] = info[number][0], ''
            time_diff = calTimeDiff(t1, t0)
            info[number][1] += time_diff
            print(time_diff)
    for i in sorted(info):
        if info[i][0]:
            answer.append(
                calFee(info[i][1]+calTimeDiff('23:59', info[i][0]), fees))
        else:
            answer.append(calFee(info[i][1], fees))
    return answer


def calTimeDiff(t2, t1):
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':'))
    return 60*(h2-h1)+(m2-m1)


def calFee(time_diff, fees):
    if time_diff <= fees[0]:
        fee = fees[1]
    else:
        fee = fees[1]+math.ceil((time_diff-fees[0])/fees[2])*fees[3]
    return fee
