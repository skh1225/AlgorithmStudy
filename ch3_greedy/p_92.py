import sys

N, M, K = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort(reverse = True)

print(M//(K+1)*(nums[0]*K+nums[1])+nums[0]*(M%(K+1)))