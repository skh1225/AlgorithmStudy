import sys
from collections import deque
input = sys.stdin.readline

INF = 2147000000
MAX_N = 401
answer = 0

# 경로 탐색 알고리즘
def BFS(source, sink, visited):
    que = deque()
    que.append(source)

    while que and visited[sink] == -1:
        sv = que.popleft()
        
		# 잔여용량이 있을 때만 해당 경로로 탐색 및 방문 체크
        for dv in graph[sv]:
            if capacity[sv][dv] - flow[sv][dv] > 0 and visited[dv] == -1:
                que.append(dv)
                visited[dv] = sv
                
				# 싱크 정점에 도달 했을 때 빠져 나옴
                if dv == sink:
                    break
	
    # 경로를 다 돌았는데 싱크를 못찾았을 경우 탐색 종료
    if visited[sink] == -1:
        return True
    else:
        return False


def edmonds_karp(source, sink):
    answer = 0
    while True:
        visited = [-1 for _ in range(MAX_N)]
        if BFS(source, sink, visited):
            break

        min_flow = INF
        
		# 탐색한 경로를 되짚어가면서 경로에 흐를 수 있는 유량을 구함 (이 문제에서는 무조건 1)
        j = sink
        while j != source:
            i = visited[j]
            min_flow = min(min_flow, capacity[i][j] - flow[i][j])
            j = i

		# 증가 경로는 유량 추가, 그리고 역방향으로 음수 유량을 추가 함
        j = sink
        while j != source:
            i = visited[j]
            flow[i][j] += min_flow
            flow[j][i] -= min_flow
            j = i
		
        # sink로 도달한 유량 총량 저장
        answer += min_flow

    return answer


N, P = map(int, input().split())

graph = [[] for _ in range(MAX_N)]
capacity = [[0]*MAX_N for _ in range(MAX_N)]
flow = [[0]*MAX_N for _ in range(MAX_N)]

for _ in range(P):
    sv, dv = map(int, input().split())
    graph[sv].append(dv)
    graph[dv].append(sv)  # 음의 유량을 고려해서 양방향으로 추가함
    capacity[sv][dv] = 1

print(edmonds_karp(1, 2))