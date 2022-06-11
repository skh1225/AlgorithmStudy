A = list(range(1,10))
del A[5]
def binarySearch(l,x):
    start = 0
    end = len(l)-1
    middle = (start+end)//2
    if x > l[-1] or x < l[0]:
        return False
    while start < end:
        if l[middle] > x:
            end = middle
        elif l[middle] < x:
            start = middle           
        else:
            return middle
        if middle == start or middle == end:
            return False
        middle = (start+end)//2
    return False
print(A)
print(binarySearch(A,6))


import sys
N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))

N_list.sort()
for i in M_list:
    start = 0
    end = N-1
    middle = (start+end)//2
    if i < N_list[0] or i > N_list[-1]:
        print('no',end=' ')
        break
    while start < end:
        if i > N_list[middle]:
            start = middle
        elif i < N_list[middle]:
            end = middle
        else:
            print('yes',end=' ')
            break
        if middle == start or middle == end:
            if i == N_list[start] or i == N_list[end]:
                print('yes',end=' ')
                break
            else:
                print('no',end=' ')
                break
        middle = (start+end)//2