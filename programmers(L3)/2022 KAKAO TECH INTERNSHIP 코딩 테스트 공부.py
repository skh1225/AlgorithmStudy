import heapq

def solution(alp, cop, problems):
    max_alp, max_cop = max(x[0] for x in problems), max(x[1] for x in problems)
    table = [[max_alp+max_cop+1 for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    problems.extend([[0,0,1,0,1],[0,0,0,1,1]])
    heap = [[0,alp,cop]]
    while heap:
        curr_cost, curr_alp, curr_cop = heapq.heappop(heap)
        if curr_alp >= max_alp and curr_cop >= max_cop:
            return curr_cost
        for r_alp, r_cop, a_alp, a_cop, a_cost in problems:
            if curr_alp >= r_alp and curr_cop >= r_cop:
                n_alp, n_cop = min(curr_alp+a_alp, max_alp), min(curr_cop+a_cop, max_cop)
                if table[n_alp][n_cop] > curr_cost + a_cost:
                    table[n_alp][n_cop] = curr_cost + a_cost
                    heapq.heappush(heap, [table[n_alp][n_cop], n_alp, n_cop])