import sys
import heapq
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(x)
res = []

for i in range(1, len(distance)):
    if distance[i] == k:
        res.append(i)

if len(res) == 0:
    print(-1)
else:
    for r in res:
        print(r)