from itertools import permutations


def solution(n, weak, dist):
    weak_len = len(weak)
    for i in weak[:]:
        weak.append(i+n)
    permutation = list(permutations(dist, len(dist)))
    answer = -1

    for per in permutation:
        for s in range(weak_len):
            start = 0
            end = 1
            for pdx, p in enumerate(per):
                while end < weak_len and weak[s+end]-weak[s+start] <= p:
                    end += 1
                start = end
                end = start + 1
                if start == weak_len:
                    if answer == -1:
                        answer = pdx+1
                    else:
                        answer = min(pdx+1, answer)
    return answer
