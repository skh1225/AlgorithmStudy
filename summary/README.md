## DFS
깊이 우선 탐색
방문 기록(visited = True/False), 방문경로(stack)
용도 : 덩어리가 몇개 인지 판단할때 등등

## BFS
너비 우선 탐색
방문 기록(visited = True/False), 방문경로(deque)
용도 : 거리 측정

## dynamic_programming
점화식 (재귀적으로 푸는 것 보다 계산량이 적음 <- 반복 계산이 줄어들어서)

## dijkstra
방문기록(visited = True/False), 최단거리(distance)
get_smallest를 통해 방문하지 않은 edge 중 가장 distance가 작은 것을 구하는 함수를 구현하거나
min heap으로 edge중 가장 distance가 작은 것을 구할 수 있음
용도 : 각 간선의 Cost가 있을 때 최단거리를 구할 때 사용

## floyd_warshall
N^3의 복잡도
용도 : 모든 경우의 최단경로를 다 구하고 싶을때
