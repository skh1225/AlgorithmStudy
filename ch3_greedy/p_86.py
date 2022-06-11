def solution(N):
    coin_types = [500,100,50,10]
    cnt = 0
    for coin in coin_types:
        cnt += N//coin
        N %= coin
    return cnt
print(solution(1260))