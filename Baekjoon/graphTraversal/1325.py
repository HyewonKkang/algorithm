import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)
visited = [False for _ in range(N + 1)]
res = []

def bfs(v):
    cnt = 1
    q = deque([v])
    visited[v] = True
    while q:
        node = q.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                q.append(n)
                cnt += 1
    return cnt


for i in range(1, N+1):
    visited = [False for _ in range(N + 1)]
    res.append(bfs(i))

max = max(res)
for i in range(len(res)):
    if max == res[i]:
        print(i+1, end=' ')
