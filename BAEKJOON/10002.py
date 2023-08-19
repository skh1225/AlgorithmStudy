import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    dist = (x2-x1)**2+(y2-y1)**2
    if dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif dist > (r1+r2)**2 or dist < (r2-r1)**2:
        print(0)
    elif dist == (r1+r2)**2 or dist == (r2-r1)**2:
        print(1)
    else:
        print(2)