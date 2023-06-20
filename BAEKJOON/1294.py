import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
words = [input().strip() for _ in range(N)]

def merge(lst):
    n = len(lst)
    if n == 1:
        return lst[0]
    if n > 2:
        mid = n//2
        return merge([merge(lst[:mid]),merge(lst[mid:])])
    result = ''
    str1, str2  = lst[0], lst[1]
    while str1 or str2:
        if str1 == '':
            result += str2
            return result
        if str2 == '':
            result += str1
            return result
        if len(str1) < len(str2):
            str1,str2 = str2,str1
        if str1[:len(str2)] > str2:
            result += str2[0]
            str2 = str2[1:]
        else:
            result += str1[0]
            str1 = str1[1:]

print(merge(words))




