n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for k in range(1, n + 1):
    upper, lower = 0, 0
    for i in range(1, n + 1):
        if i == k: continue
        if graph[k][i] != INF:
            upper += 1

    for i in range(1, n + 1):
        if i == k: continue
        if graph[i][k] != INF:
            lower += 1

    if upper + lower == n - 1:
        answer += 1
print(answer)
