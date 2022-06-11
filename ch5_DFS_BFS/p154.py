from collections import deque

len_m = 3
len_n = 3
# graph = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
graph = [[1,1,0],[0,1,0],[0,1,1]]
cnt = 0
def BFS(m,n):
    queue = deque([(m,n)])
    tmp = deque()
    graph[m][n] = 0
    cnt = 1
    while queue:
        for m_,n_ in queue:
            for m__, n__ in zip([m_,m_,m_-1,m_+1],[n_-1,n_+1,n_,n_]):
                if -1 < m__ and m__ < len_m and -1 < n__ and n__ < len_n and graph[m__][n__] == 1:
                    tmp.append((m__,n__)
                    graph[m__][n__] = 0
                    if (m__,n__) == (len_m-1, len_n-1):
                        return cnt+1
        queue = tmp
        tmp = deque()
        cnt += 1

print(BFS(0,0))
