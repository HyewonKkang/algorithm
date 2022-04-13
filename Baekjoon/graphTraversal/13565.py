from collections import deque
m, n = map(int, input().split())
grid = [list(map(int, list(input()))) for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if grid[nx][ny] == 0:
                    grid[nx][ny] = 2
                    q.append((nx, ny))

for i in range(n):
    if grid[0][i] == 0:
        bfs(0, i)
flag = 0
for i in range(n):
    if grid[m - 1][i] == 2:
        flag = 1
if flag == 0:
    print("NO")
else:
    print("YES")