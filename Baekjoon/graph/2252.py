import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
problems = [0 for _ in range(N+1)]
graph = {}
for _ in range(M):
    first, second = map(int, sys.stdin.readline().split())
    problems[second] += 1
    if first in graph:
        graph[first].append(second)
    else:
        graph[first] = [second]
dq = deque()
for i in range(1, N+1):
    if problems[i] == 0:
        dq.append(i)
res = []
while dq:
    n = dq.popleft()
    res.append(n)
    if n in graph:
        for j in graph[n]:
            problems[j] -= 1
            if problems[j] == 0:
                dq.append(j)
print(*res)
