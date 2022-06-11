import sys
N = int(sys.stdin.readline())
M = list(sys.stdin.readline().split())
x = 1
y = 1
for c in M:
    if c == 'R':
        if x != N:
            x += 1
    elif c == 'L':
        if x != 1:
            x -= 1
    elif c == 'U':
        if y != 1:
            y -= 1
    elif c == 'D':
        if y != N:
            y += 1

print(y, x)