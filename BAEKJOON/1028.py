import sys
input = sys.stdin.readline

R, C = map(int,input().split())
graph1 = [input().strip() for _ in range(R)]
graph2 = [[[0,0] for _ in range(C)] for _ in range(R)]

def check(r, c, R=R, C=C):
    answer = 1
    while True:
        if r+answer < R and c+answer < C and c-answer >= 0:
            if graph1[r+answer][c+answer] == '1' and graph1[r+answer][c-answer] == '1':
                answer += 1
            else:
                break
        else:
            break
    graph2[r][c][0] = answer
    answer = 1
    while True:
        if r-answer >= 0 and c+answer < C and c-answer >= 0:
            if graph1[r-answer][c+answer] == '1' and graph1[r-answer][c-answer] == '1':
                answer += 1
            else:
                break
        else:
            break
    graph2[r][c][1] = answer

for r in range(R):
    for c in range(C):
        if graph1[r][c] == '1':
            check(r, c)

answer = 0
for r in range(R):
    for c in range(C):
        if graph2[r][c][0] > answer:
            for k in range(graph2[r][c][0],answer,-1):
                if r+2*(k-1) < R and graph2[r+2*(k-1)][c][1] >= k:
                    answer = k
                    break
print(answer)