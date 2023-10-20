from collections import deque
n, m = map(int, input().split())
answer = [[0] * m for _ in range(n)]
maps = []
visited = [[False] * m for _ in range(n)]
goal = None
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if not goal and row[j] == 2:
            goal = (i, j)
    maps.append(row)

def bfs(x, y, answer):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if maps[nx][ny] > 0 and not visited[nx][ny]:
                answer[nx][ny] = answer[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))


answer = [[0] * m for _ in range(n)]
bfs(goal[0], goal[1], answer)

for i in range(n):
    for j in range(m):
        if answer[i][j] == 0 and maps[i][j] > 0:
            answer[i][j] = -1
answer[goal[0]][goal[1]] = 0

for row in answer:
    print(*row)