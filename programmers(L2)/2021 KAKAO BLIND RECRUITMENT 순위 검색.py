import re

def solution(info, query):
    answer = []
    Info = dict()
    for i in info:
        tmp = i.split()
        score = int(tmp[-1])
        condition = ''.join([t[0] for t in tmp[:-1]])
        Info[condition] = Info.get(condition,[]) + [score]
        
    for I in Info:
        Info[I].sort()
        
    for q in query:
        tmp = re.split(' and | ', q)
        score = int(tmp[-1])
        condition = ''.join(['.' if t[0]=='-' else t[0] for t in tmp[:-1]])
        cnt = 0
        p = re.compile(condition)
        for key in Info:
            if p.match(key):
                cnt += det(score,Info[key])
        answer.append(cnt)
    return answer

def det(score,Info):
    start = 0
    end = len(Info)-1
    if Info[start]>=score:
        return len(Info)
    elif Info[end]<score:
        return 0
    while start < end-1:
        mid = (start+end)//2
        if Info[mid] >= score:
            end = mid
        else:
            start = mid
    return len(Info)-end