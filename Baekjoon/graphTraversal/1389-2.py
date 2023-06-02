# 플로이드 워셜 풀이
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = []
for i in range(1, n + 1):
    result.append(sum(graph[i][1:]))

print(result.index(min(result)) + 1)