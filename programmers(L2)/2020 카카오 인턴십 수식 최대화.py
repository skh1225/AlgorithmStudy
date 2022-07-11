from itertools import permutations

def solution(expression):
    answer = 0
    operations = permutations('+-*', 3)
    for operation in operations:
        tmp = []
        for ex in expression.split(operation[0]):
            tmp.append(operation[1].join(
                [f'({e})' for e in ex.split(operation[1])]))
        tmp_ex = operation[0].join([f'({t})' for t in tmp])
        answer = max(answer, abs(eval(tmp_ex)))
        print(operation, tmp, tmp_ex)
    return answer