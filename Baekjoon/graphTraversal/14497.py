from collections import deque
n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
area = [list(input()) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]


def bfs(x, y):
    q = deque([(x, y)])
    distance[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if distance[nx][ny] == -1:
                if area[nx][ny] == '0':
                    distance[nx][ny] = distance[x][y]
                    q.appendleft((nx, ny))
                elif area[nx][ny] == '1' or area[nx][ny] == '#':
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

bfs(x1 - 1, y1 - 1)
print(distance[x2 - 1][y2 - 1])