import re

def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    Str1, Str2 = dict(), dict()
    p = re.compile('^[a-z]{2}$')
    cnt = 0
    for i in range(len(str1)-1):
        if p.match(str1[i:i+2]):
            Str1[str1[i:i+2]] = Str1.get(str1[i:i+2],0)+1
            cnt += 1
            
    for j in range(len(str2)-1):
        if p.match(str2[j:j+2]):
            Str2[str2[j:j+2]] = Str2.get(str2[j:j+2],0)+1
            cnt += 1
    intersection = 0        
    for key in Str1:
        if key in Str2:
            intersection += min(Str1[key],Str2[key])
    if cnt:
        return int(65536*intersection/(cnt-intersection))
    else:
        return 65536