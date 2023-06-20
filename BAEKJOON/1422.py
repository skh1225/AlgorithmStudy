import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = []
max_num = 0
for _ in range(K):
    num = input().strip()
    arr.append(num)
    max_num = max(max_num, int(num))

for _ in range(N-K):
    arr.append(str(max_num))

arr.sort(key=lambda x : x*10,reverse=True)
print(''.join(arr))

