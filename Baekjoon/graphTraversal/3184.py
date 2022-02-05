import sys
from collections import deque

R, C = map(int, sys.stdin.readline().rstrip().split())
field = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
res_s = 0
res_w = 0


def bfs(x, y):
    s, w = [0, 0]
    q = deque()
    q.append([x, y])
    if field[x][y] == 'v':
        w += 1
    elif field[x][y] == 'o':
        s += 1
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if field[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    if field[nx][ny] == 'v':
                        w += 1
                    elif field[nx][ny] == 'o':
                        s += 1
    if s == w == 0:
        return [0, 0]
    elif s > w:
        return [s, 0]
    else:
        return [0, w]


for i in range(R):
    for j in range(C):
        if field[i][j] != '#' and not visited[i][j]:
            s, w = bfs(i, j)
            res_s += s
            res_w += w
print(res_s, res_w)
