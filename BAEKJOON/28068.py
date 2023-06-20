import sys

N = int(sys.stdin.readline())

plus_books, minus_books = [], []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a-b <= 0 :
        plus_books.append((a,b))
    else:
        minus_books.append((b,a))
plus_books.sort()
minus_books.sort()


def plus_peak(books):
    v = 0
    for book in books:
        a,b = book
        v -= a
        if v < 0:
            return -1
        v += b
    return v

def minus_peak(books, limit):
    v = 0
    for book in books:
        a,b = book
        v -= a
        if v < 0:
            v = 0
        v += b
        if v > limit:
            return -1
    if v > limit:
            return -1
    return v

if minus_peak(minus_books, plus_peak(plus_books)) >= 0:
    print(1)
else:
    print(0)