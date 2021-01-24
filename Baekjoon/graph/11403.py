N = int(input())
visited = [0 for i in range(N)]
graph = []
matrix = [[0] * N for i in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

def dfs(root):
    for i in range(N):
        if visited[i] == 0 and graph[root][i] == 1:
            visited[i] = 1
            dfs(i)

for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

    visited = [0 for i in range(N)]

    for j in range(N):
        print(matrix[i][j], end = ' ')
    print()


