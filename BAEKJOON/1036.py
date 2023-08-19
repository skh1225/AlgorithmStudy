import sys
input = sys.stdin.readline

f = lambda x:int(x) if x<='9' else ord(x)-ord('A')+10
F = lambda x:str(x) if x<=9 else chr(x-10+ord('A'))
record = [[0 for _ in range(52)] for _ in range(36)]
answer = [0 for _ in range(52)]

def calc(lst1, lst2):
    l = 52
    if len(lst2) < l:
        l = len(lst2)
    for i in range(l):
        answer[51-i] += lst2[l-1-i]
        if answer[51-i] >= 36:
            answer[51-i] %= 36
            answer[50-i] += 1
        if i == l-1:
            for j in range(l,52):
                if answer[51-j] >= 36:
                    answer[51-j] %= 36
                    answer[50-j] += 1
                else:
                    break

for _ in range(int(input())):
    x = list(map(f,list(input().strip().lstrip('0'))))
    calc(answer,x)
    l = len(x)
    for i in range(l):
        c = x[l-1-i]
        record[c][51-i] += 35-c
        tmp = 51-i
        while record[c][tmp] >= 36:
            record[c][tmp] %= 36
            record[c][tmp-1] += 1
            tmp -= 1

record.sort(reverse=True)

for k in range(int(input())):
    calc(answer,record[k])

result = ''

for a in answer:
    if a == 0 and not result:
        continue
    result += F(a)

if result:
    print(result)
else:
    print('0')