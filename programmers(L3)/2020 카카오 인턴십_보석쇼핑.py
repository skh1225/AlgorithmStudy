def solution(gems):
    answer = [0, 0]
    category = dict()
    for g in gems:
        if len(category) == 0:
            category[g] = 1
            result = answer[:]
            continue
        if g not in category:
            answer[1] += 1
            category[g] = 1
            result = answer[:]
        else:
            answer[1] += 1
            category[g] += 1
            while answer[1]-answer[0] > 0 and category[gems[answer[0]]] > 1:
                category[gems[answer[0]]] -= 1
                answer[0] += 1
            if result[1]-result[0] > answer[1]-answer[0]:
                result = answer[:]

    return [result[0]+1, result[1]+1]
