from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
shortestPath = [-1] * (n + 1)
shortestPath[x] = 0


def bfs(x):
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if shortestPath[i] == -1:
                q.append(i)
                shortestPath[i] = shortestPath[now] + 1


bfs(x)

answer = -1
for i in range(len(shortestPath)):
    if shortestPath[i] == k:
        print(i)
        answer += 1
if answer == -1:
    print(-1)