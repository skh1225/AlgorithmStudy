import sys
input = sys.stdin.readline

queries = []
standard = set()

for _ in range(int(input())):
    x = tuple(map(int,input().split()))
    queries.append(x)
    if x[0] == 2:
        standard.add(x[1])

standard = sorted(list(standard))
N = len(standard)
FW = [0 for _ in range(2*N+1)]

def binary_search(x):
    s,e = 0, len(standard)-1
    while s <= e:
        mid = (s+e)//2
        if standard[mid] == x:
            return 2*mid+1
        elif standard[mid] > x:
            e = mid-1
        else:
            s = mid+1
    return 2*s

def update(i):
    while i <= 2*N:
        FW[i] += 1
        i += (i & -i)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += FW[i]
        i -= (i & -i)
    return result

def get_value(i):
    return prefix_sum(i)-prefix_sum(i-1)

sign = 1
total = 0
for Q in queries:
    if Q[0] == 1:
        a, b = Q[1:]
        if a == 0:
            sign *= b/abs(b) if b!=0 else 0
            continue
        else:
            sign *= a/abs(a)
            index = binary_search(-b/a)
            total += 1
            update(index)
    else:
        if sign == 0:
            print('0')
            continue
        index = binary_search(Q[1])
        if get_value(index) > 0:
            print('0')
        else:
            result = sign if (total-prefix_sum(index))%2 == 0 else -sign
            if result > 0:
                print('+')
            else:
                print('-')