import sys
INF = int(1e9)
input = sys.stdin.readline
n = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            graph[i + 1][j + 1] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

res = [[0] * n for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] < INF:
            res[i - 1][j - 1] = 1

for i in range(n):
    for j in range(n):
        print(res[i][j], end = ' ')
    print()