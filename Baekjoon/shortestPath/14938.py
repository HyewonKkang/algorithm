n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)] # (dist, item)

for i in range(1, n + 1):
    graph[i][i] = 0

for i in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            tmp += items[j]
    answer = max(answer, tmp)

print(answer)


