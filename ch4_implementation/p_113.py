import sys
N = int(sys.stdin.readline())
per_hour = 15*60 + 15*45
result = N*per_hour
if N > 3:
    result += 60*60
else:
    result += per_hour
print(result)