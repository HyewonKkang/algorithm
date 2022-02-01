N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
res = 0

def dfs(x, y):
    if 0 <= x < N and 0 <= y < M:
        if graph[x][y] == 0 and not visited[x][y]:
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            res += 1
print(res)