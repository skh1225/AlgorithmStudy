import sys
input = sys.stdin.readline

N = int(input())
W = int(input())

node = [(1,1)]
for _ in range(W):
    node.append(tuple(map(int,input().split())))

def get_distance(x,y):
    return abs(node[x][0]-node[y][0])+abs(node[x][1]-node[y][1])

INF = int(1e7)
dp1, dp2 = [[[INF,(0,0)] for _ in range(W+1)] for _ in range(W+1)], [[[INF,(0,0)] for _ in range(W+1)] for _ in range(W+1)]
dp1[1][0][0], dp2[1][0][0] = get_distance(0,1), 2*(N-1)-get_distance(0,1)

for i in range(1,W):
    for j in range(i):
        dp1[i+1][j][0], dp2[i+1][j][0] = dp1[i][j][0]+get_distance(i,i+1), dp2[i][j][0]+get_distance(i,i+1)
        if j == 0:
            dp1[i+1][i][0] = dp2[i][0][0]+get_distance(0,i+1)
            dp2[i+1][i][0] = dp1[i][0][0]+2*(N-1)-get_distance(0,i+1)
            dp1[i+1][i][1], dp2[i+1][i][1] = (j,i), (i,j)
        else:
            if dp1[i+1][i][0] > dp2[i][j][0]+get_distance(j,i+1):
                dp1[i+1][i][0] = dp2[i][j][0]+get_distance(j,i+1)
                dp1[i+1][i][1] = (j,i)
            if dp2[i+1][i][0] > dp1[i][j][0]+get_distance(j,i+1):
                dp2[i+1][i][0] = dp1[i][j][0]+get_distance(j,i+1)
                dp2[i+1][i][1] = (i,j)
answer = INF
curr = (0,0)
for i in range(W+1):
    if answer > dp1[W][i][0]:
        answer = dp1[W][i][0]
        curr = (W,i)
    if answer > dp2[W][i][0]:
        answer = dp2[W][i][0]
        curr = (i,W)

print(answer)
record = ''
while curr != (0,0):
    if curr[0] > curr[1]:
        record = '1\n'*(curr[0]-curr[1]) + record
        curr = dp1[curr[1]+1][curr[1]][1]
    else: 
        record = '2\n'*(curr[1]-curr[0]) + record
        curr = dp2[curr[0]+1][curr[0]][1]
print(record)

