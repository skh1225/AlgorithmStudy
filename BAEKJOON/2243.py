import sys
input = sys.stdin.readline

MAX = 2**20
tree = [0 for _ in range(MAX+1)]

def update(i, v):
    while i <= MAX:
        tree[i] += v
        i += (i & -i)

def find(r):
    start, value = 2**19, tree[2**19]
    for i in reversed(range(20)):
        if value >= r:
            value -= tree[start]
            start -= 2**i
        else:
            start += 2**i
        value += tree[start]
    if value < r:
        return start+1
    else:
        return start
    
for _ in range(int(input())):
    command = tuple(map(int,input().split()))
    if command[0] == 1:
        answer = find(command[1])
        update(answer, -1)
        print(answer)
    else:
        update(command[1], command[2])


        

