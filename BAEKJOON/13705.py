import math
from decimal import *
A,B,C = map(int, input().split())
getcontext().prec = 50
R = Decimal(C)/Decimal(A)
PI = Decimal('3.14159265358979323846264338327950288419716939937510')

def sin(x):
    x %= 2*PI
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def fun(x):
    return Decimal(A)*x+Decimal(B)*sin(x+R)

x,y = Decimal(0),Decimal(2)

while x+R-(x+R)%Decimal('0.0000001')+y > Decimal('0.0000001'):
    y /= 2
    cal = fun(x)
    if cal > 0:
        x -= y
    elif cal < 0:
        x += y
    else:
        break

print(round(x+R,6))