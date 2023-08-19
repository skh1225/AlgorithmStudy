import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

def check():
    tmp = []
    s,e = 0,1
    while True:
        if e == N:
            tmp.append((s,e-1))
            break
        if arr[e] == arr[s]+1:
            e += 1
        else:
            tmp.append((s,e-1))
            s = e; e = s+1
    return tmp

is_end = check()
record = []
while len(is_end) > 1:
    breaker = False
    for i in range(N):
        for j in range(i+1,N):
            if 1-arr[i] == arr[j]:
                record.append((i+1,j))
                start, end = i,j-1
                while start < end:
                    arr[start],arr[end] = -arr[end], -arr[start]
                    start += 1
                    end -= 1
                if start == end:
                    arr[start] = -arr[start]
                breaker = True
                break
        if breaker:
            break
    else:
    is_end = check()

print(len(record))
for k in reversed(range(len(record))):
    print(' '.join(map(str,record[k])))



