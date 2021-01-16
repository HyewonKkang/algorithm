import heapq, sys
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
heap = []
for i in range(1, N+1):
    if problems[i] == 0:
        heapq.heappush(heap, i)
res = []
while heap:
    n = heapq.heappop(heap)
    res.append(n)
    if n in graph:
        for j in graph[n]:
            problems[j] -= 1
            if problems[j] == 0:
                heapq.heappush(heap, j)
print(*res)
