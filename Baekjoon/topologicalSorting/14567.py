from collections import deque
n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
result = [1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = deque([])

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append((i, 1))

    while q:
        now, term = q.popleft()
        result[now] = term
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i, term + 1))

topology_sort()
print(*result[1:])