def solution(places):
    answer = []
    for p in places:
        breaker = False
        for m in range(5):
            for n in range(5):
                if p[m][n] == 'P':
                    if det(p,m,n):
                        continue
                    else:
                        answer.append(0)
                        breaker = True
                        break
            if breaker:
                break
        else:
            answer.append(1)
    return answer

def det(p,m,n):
    for M in range(m-2,m+3):
        for N in range(n-2+abs(M-m),n+3-abs(M-m)):
            if M == m and N == n or M > 4 or N > 4 or M < 0 or N < 0:
                continue
            if p[M][N] == 'P':
                if abs(M-m) + abs(N-n) == 1:
                    return False
                else:
                    if abs(M-m) == 2 and p[(M+m)//2][N] != 'X':
                        return False
                    elif abs(N-n) == 2 and p[M][(n+N)//2] != 'X':
                        return False
                    elif abs(M-m) == abs(N-n) and (p[m][N] != 'X' or p[M][n] != 'X'):
                        return False
    return True