from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    q = deque([(0, 0)])
    count = 0
    visited = [[False] * m for _ in range(n)]
    while q:
        x, y = q.popleft()
        for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or 0 < ny < 0 or ny >= m: continue
            if visited[nx][ny]: continue
            if arr[nx][ny]:
                arr[nx][ny] = 0
                count += 1
            else:
                q.append((nx, ny))
            visited[nx][ny] = True
    return count

t = 0
cheeses = []
while True:
    t += 1
    count = bfs()
    cheeses.append(count)
    if count == 0: break

print(t - 1)
print(cheeses[-2])