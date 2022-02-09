import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

for case in range(t):
    l = int(sys.stdin.readline().rstrip())
    s_x, s_y = map(int, input().split())
    d_x, d_y = map(int, input().split())
    grid = [[0] * l for _ in range(l)]

    q = deque()
    q.append((s_x, s_y))
    grid[s_x][s_y] = 1
    while q:
        x, y = q.popleft()
        if x == d_x and y == d_y:
            print(grid[x][y] - 1)
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and grid[nx][ny] == 0:
                q.append((nx, ny))
                grid[nx][ny] = grid[x][y] + 1