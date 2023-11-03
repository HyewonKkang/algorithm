import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [int(1e9) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
heapq.heappush(q, (0, 1))
while q:
    cost, loc = heapq.heappop(q)
    distance[0] = 0
    if distance[loc] < cost:
        continue
    for near in graph[loc]:
        next = cost + near[1]
        if next < distance[near[0]]:
            distance[near[0]] = next
            heapq.heappush(q, (next, near[0]))
print(distance)
print(distance[n])
