# 문제 4
# import sys
# N, M = map(int, sys.stdin.readline().split())
# money = [int(sys.stdin.readline()) for _ in range(N)]
# INF = int(1e4)+1
# result = [INF]*(M+1)
# result[0] = 0
# for i in range(N):
#     for j in range(money[i], M+1):
#         if result[j-money[i]] == INF:
#             continue
#         result[j] = min(result[j-money[i]]+1, result[j])
# if result[M] == INF:
#     print(-1)
# else:
#     print(result[M])


# 문제 3
# import sys
# N = int(sys.stdin.readline())
# result = [0]*(N+1)
# result[0] = 1
# for i in range(1, N+1):
#     if i == 1:
#         result[i] = 1
#     else:
#         result[i] = result[i-2]*2+result[i-1]
# print(result[N])


# 문제 2
# import sys

# N = int(sys.stdin.readline())
# food = list(map(int, sys.stdin.readline().split()))
# result = []
# for idx, v in enumerate(food):
#     if idx == 0:
#         result.append(v)
#     elif idx == 1:
#         result.append(max(v, result[0]))
#     else:
#         result.append(max(v+result[idx-2], result[idx-1]))
# print(result[N-1])


# 문제 1
# import sys
# INF = int(1e9)
# X = int(sys.stdin.readline())
# # Y = [INF for _ in range(X+1)]
# Y = [0 for _ in range(X+1)]
# Y[1] = 0

# for i in range(2, X+1):
#     Y[i] = Y[i-1] + 1
#     if i % 5 == 0:
#         Y[i] = min(Y[i//5]+1, Y[i])
#     if i % 3 == 0:
#         Y[i] = min(Y[i//3]+1, Y[i])
#     if i % 2 == 0:
#         Y[i] = min(Y[i//2]+1, Y[i])
# print(Y[X])
