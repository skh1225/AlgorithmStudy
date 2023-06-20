def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery, pickup = [], []
    d, p = 0,0
    for i in reversed(range(n)):
        if deliveries[i] > 0:
            if d == 0:
                delivery.append(i+1)
            d += deliveries[i]
            while d > cap:
                delivery.append(i+1)
                d -= cap
        if pickups[i] > 0:
            if p == 0:
                pickup.append(i+1)
            p += pickups[i]
            while p > cap:
                pickup.append(i+1)
                p -= cap
    if len(delivery) > len(pickup):
        for i in range(len(pickup)):
            answer += max(delivery[i], pickup[i])
        answer += sum(delivery[len(pickup):])
    else:
        for i in range(len(delivery)):
            answer += max(delivery[i], pickup[i])
        answer += sum(pickup[len(delivery):]) 
    return answer*2