def solution(p):
    return bracketsTransformer(p)
def bracketsTransformer(s):
    result = ''
    if not s:
        return ''
    cnt = 0
    det = False
    for idx, c in enumerate(s):
        if idx == 0 and c == '(':
            det = True
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            break
    u = s[:idx+1]
    v = s[idx+1:]
    if det:
        if v:
            result = u+bracketsTransformer(v)
        else:
            result = u
    else:
        if v:
            result = '('+bracketsTransformer(v)+')'
        else:
            result = '()'
        for j in u[1:-1]:
            if j == '(':
                result += ')'
            else:
                result += '('
    return result