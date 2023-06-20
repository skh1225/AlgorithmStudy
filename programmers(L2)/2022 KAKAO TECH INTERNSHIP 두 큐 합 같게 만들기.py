from collections import deque

def solution(queue1, queue2):
    length = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    total = sum(queue1)+sum(queue2)
    if total%2==1:
        return -1
    trial = 0
    diff = sum(queue1) - total/2
    while trial < (3*length-2):
        if diff > 0:
            e = queue1.popleft()
            diff -= e
            queue2.append(e)
            trial += 1
        elif diff < 0:
            e = queue2.popleft()
            diff += e
            queue1.append(e)
            trial += 1
        else:
            return trial
    return -1
            
    