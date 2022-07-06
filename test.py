from itertools import combinations


def solution(relation):
    answer = 0
    row = len(relation)
    column = len(relation[0])
    info = []
    for n in range(column):
        tmp = []
        memory = []
        for m in range(row):
            if relation[m][n] in memory:
                continue
            tmp_set = set([m])
            for i in range(m+1, row):
                if relation[m][n] == relation[i][n]:
                    tmp_set.add(i)
            if len(tmp_set) > 1:
                tmp.append(tmp_set)
                memory.append(relation[m][n])
        info.append(tmp)
    memory = []
    for i in range(len(info)):
        if len(info[i]) == 0:
            memory.append(set([i]))
    for i in range(2, len(info)+1):
        combination = list(combinations(range(len(info)), i))
        for com in combination:
            breaker = False
            tmp = []
            for m in memory:
                if m.issubset(set(com)):
                    breaker = True
                    break
            if breaker:
                continue
            for c in com:
                if tmp:
                    temp = []
                    for t in tmp:
                        for Info in info[c]:
                            print(t, Info)
                            if len(t & Info) > 1:
                                temp.append(t & Info)
                    tmp = temp
                else:
                    tmp = info[c]
            if len(temp) == 0:
                memory.append(set(com))
    print(info)
    print(memory)
    return len(memory)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
      "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
