def solution(tickets):
    answer = ["ICN"]
    stack = []
    tickets.sort(reverse=True)
    graph = dict()
    for t in tickets:
        graph[t[0]] = graph.get(t[0], [])
        graph[t[0]].append(t[1])
    while len(answer)+len(stack) < len(tickets)+1:
        if answer[-1] not in graph or len(graph[answer[-1]]) == 0:
            stack.append(answer.pop())
            continue
        answer.append(graph[answer[-1]].pop())
    stack.reverse()
    return answer + stack
