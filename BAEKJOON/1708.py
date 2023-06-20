import sys
input = sys.stdin.readline

N = int(input())
visited = [False for _ in range(N)]
nodes = []
start = -1
for n in range(N):
    x, y = map(int,input().split())
    if start == -1:
        start = n
    else:
        x1, y1 = nodes[start]
        if y1 > y or (y1 == y and x1 > x):
            start = n
    nodes.append((x, y))

def find(c_v, start=start,  N=N):
    n_v = -1
    for n in range(N):
        if not visited[n] and n != c_v:
            x1, y1 = nodes[c_v][0]-nodes[start][0], nodes[c_v][1]-nodes[start][1]
            x2, y2 = nodes[n][0]-nodes[start][0], nodes[n][1]-nodes[start][1]
            if x1*y2-x2*y1 < 0:
                visited[n] = True
            else:
                if n_v == -1:
                    n_v = n
                else:
                    x1, y1 = nodes[n_v][0]-nodes[c_v][0], nodes[n_v][1]-nodes[c_v][1]
                    x2, y2 = nodes[n][0]-nodes[c_v][0], nodes[n][1]-nodes[c_v][1]
                    if x1*y2-x2*y1 < 0:
                        n_v = n
                    elif x1*y2-x2*y1 == 0:
                        if abs(x1)+abs(y1) < abs(x2)+abs(y2):
                            visited[n_v] = True
                            n_v = n
                        else:
                            visited[n] = True
    visited[n_v] = True
    return n_v

n_v = find(start)
answer = 0
while n_v != -1:
    n_v = find(n_v)
    answer += 1
print(answer)

    