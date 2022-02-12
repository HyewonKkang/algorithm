import sys
T = int(sys.stdin.readline().rstrip())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
sys.setrecursionlimit(1000000)

def dfs(field, x, y):
    field[x][y] = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
            dfs(field, nx, ny)


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    field = [[0] * M for _ in range(N)]
    res = 0
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        field[b][a] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                dfs(field, i, j)
                res += 1
    print(res)
