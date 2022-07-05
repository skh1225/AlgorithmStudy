from datetime import datetime, timedelta

def solution(lines):
    answer = 0
    stack = []
    for l in lines:
        end = datetime.strptime(l[:23],'%Y-%m-%d %H:%M:%S.%f')
        seconds = int(l[24:-1].split('.')[0])
        milliseconds = 0
        if '.' in l[24:-1]:
            milliseconds = int(l[24:-1].split('.')[1]+'0'*(3-len(l[24:-1].split('.')[1])))
        start = end - timedelta(seconds = seconds+1,milliseconds=milliseconds-2)
        stack.append((start,'A'))
        stack.append((end,'Z'))
    stack.sort()
    cnt = 0
    for s in stack:
        if s[1] == 'A':
            cnt += 1
        else:
            answer = max(answer,cnt)
            cnt -= 1
    return answer