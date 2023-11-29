from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

    dst = maps[n-1][m-1]
    return dst if dst > 1 else -1
