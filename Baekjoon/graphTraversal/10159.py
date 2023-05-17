n = int(input())
m = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

for k in range(1, n + 1):
    count = 0
    for i in range(1, n + 1):
        count += graph[k][i] + graph[i][k]
    print(n - count - 1)

