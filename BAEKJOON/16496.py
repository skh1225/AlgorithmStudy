import sys
input = sys.stdin.readline

N = int(input())
ARR = input().split()

ARR.sort(key = lambda x:(x*10)[:10],reverse=True)

if ARR[0][0] == '0':
    print(0)
else:
    print(''.join(ARR))