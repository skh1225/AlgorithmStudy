import re


def solution(info, query):
    answer = []
    count = dict()
    score = []
    for idx, i in enumerate(info):
        Info = i.split()
        score.append(int(Info.pop()))
        for I in Info:
            count[I] = count.get(I, [])+[idx]

    for q in query:
        Query = re.split(' and | ', q)
        tmp = set(range(len(info)))
        for j in range(4):
            if Query[j] != '-':
                tmp = tmp & set(count[Query[j]])
        if Query[4] != '-':
            answer.append(len(tmp))
        else:
            cnt = 0
            for t in tmp:
                if score[t] >= Query[4]:
                    cnt += 1
            answer.append(cnt)
    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
