import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
time = []

for i in range(n):
    time.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i + 1][j + 1] = 0
        elif time[i][j] > 0:
            graph[i + 1][j + 1] = time[i][j]

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")


