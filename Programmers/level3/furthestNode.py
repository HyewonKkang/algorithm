import heapq
def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]
    distance = [int(1e9)] * (n + 1)
    for v in vertex:
        a, b = v
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, node = heapq.heappop(q)
            if distance[node] < dist:
                continue
            for i in graph[node]:
                cost = i[1] + dist
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(1)
    max_value = max(distance[1:])
    return distance.count(max_value)
