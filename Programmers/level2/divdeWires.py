from collections import deque
from itertools import combinations

def solution(n, wires):
    answer = int(1e9)
    l = len(wires)

    def getGraph(wires_set):
        graph = {i: [] for i in range(1, n + 1)}
        for wire in wires_set:
            a, b = wire
            graph[a].append(b)
            graph[b].append(a)
        return graph

    def countWires(node, graph, visited):
        q = deque([node])
        visited[node] = True
        count = 0
        while q:
            node = q.popleft()
            for near in graph[node]:
                if not visited[near]:
                    q.append(near)
                    visited[near] = True
                    count += 1
        return count, graph, visited

    for combs in list(combinations(wires, l - 1)):
        visited = [False] * (n + 1)
        tmp = []
        graph = getGraph(combs)
        for i in range(1, n + 1):
            if not visited[i]:
                count, graph, visited = countWires(i, graph, visited)
                tmp.append(count)
        answer = min(answer, abs(tmp[0] - tmp[1]))
    return answer
