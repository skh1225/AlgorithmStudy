import re


def solution(user_id, banned_id):
    answer = []
    ban = [[] for _ in range(len(banned_id))]
    for bidx, b in enumerate(banned_id):
        tmp = '^'
        for c in b:
            if c == '*':
                tmp += '[a-z0-9]'
            else:
                tmp += c
        tmp += '$'
        det = re.compile(tmp)
        for uidx, u in enumerate(user_id):
            if det.match(u):
                ban[bidx].append(uidx)
    result = [set()]
    for i in range(len(ban)):
        tmp = []
        for j in ban[i]:
            for r in result[:]:
                tmp.append(r | set([j]))
        result = tmp
    for r in result:
        print(len(ban))
        if r not in answer and len(r) == len(ban):
            answer.append(r)
    return answer


print(solution(["frodo", "fradi", "crodo",
      "abc123", "frodoc"], ["fr*d*", "abc1**"]))
