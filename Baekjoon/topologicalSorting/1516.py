from collections import deque
n = int(input())
graph = [[] for _ in range(n + 1)]
durations = [0] * (n + 1)
indegree = [0] * (n + 1)
result = [0] * (n + 1)

for i in range(1, n + 1):
    lst = list(map(int, input().split()))[:-1]
    durations[i] = lst[0]
    pre = lst[1:]
    for p in pre:
        graph[p].append(i)
        indegree[i] += 1

def topology_sort():
    q = deque([])

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = durations[i]

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + durations[i])

            if indegree[i] == 0:
                q.append(i)

topology_sort()
for r in result[1:]:
    print(r)