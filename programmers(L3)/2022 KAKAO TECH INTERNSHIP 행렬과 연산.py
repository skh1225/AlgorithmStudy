from collections import deque

def solution(rc, operations):
    answer = [[] for _ in range(len(rc))]
    mid_pillar, left_pillar, right_pillar = deque(), deque(), deque()
    for r in rc:
        mid_pillar.append(deque(r[1:-1]))
        left_pillar.append(r[0])
        right_pillar.append(r[-1])
    for op in operations:
        if op == 'Rotate':
            if mid_pillar:
                mid_pillar[0].appendleft(left_pillar.popleft())
                right_pillar.appendleft(mid_pillar[0].pop())
                mid_pillar[-1].append(right_pillar.pop())
                left_pillar.append(mid_pillar[-1].popleft())
            else:
                right_pillar.appendleft(left_pillar.popleft())
                left_pillar.append(right_pillar.pop())
        else:
            mid_pillar.rotate(1)
            left_pillar.rotate(1)
            right_pillar.rotate(1)
    for i in range(len(rc)):
        answer[i].append(left_pillar[i])
        if mid_pillar:
            answer[i].extend(list(mid_pillar[i]))
        answer[i].append(right_pillar[i])
    return answer