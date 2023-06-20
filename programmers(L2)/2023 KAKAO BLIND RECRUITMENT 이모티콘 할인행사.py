from itertools import product
import math
def solution(users, emoticons):
    answer = [0,0]
    info = [[] for _ in range(4)]
    for user in users:
        info[math.ceil(user[0]/10)-1].append(user[1])
    for i in range(4):
        info[i].sort()
    for p in product(range(1,5), repeat=len(emoticons)):
        tmp = [0 for _ in range(4)]
        for i in range(len(emoticons)):
            for j in range(p[i]):
                tmp[j] += emoticons[i]*(10-p[i])/10
        member, money = 0,0
        for i in range(4):
            for j in info[i]:
                if j > tmp[i]:
                    money += tmp[i]
                else:
                    member += 1
        answer = max(answer, [member, money])
    return answer