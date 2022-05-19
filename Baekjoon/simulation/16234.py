from collections import deque
import sys

input = sys.stdin.readline
n, l, r = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]
days = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    borders = {}
    opened = False
    for i in range(n):
        for j in range(n):
            for k in range(4):
                neighbor_x, neighbor_y = i + dx[k], j + dy[k]
                if 0 <= neighbor_x < n and 0 <= neighbor_y < n:
                    if l <= abs(population[i][j] - population[neighbor_x][neighbor_y]) <= r:
                        if (i, j) in borders:
                            borders[(i, j)].append((neighbor_x, neighbor_y))
                        else:
                            borders[(i, j)] = [(neighbor_x, neighbor_y)]
                        opened = True

    if not opened:
        break

    visited = [[False] * n for _ in range(n)]

    def bfs(start_x, start_y):
        dx2 = [0, 1, 0, -1]
        dy2 = [1, 0, -1, 0]
        queue = deque([(start_x, start_y)])
        visited[start_x][start_y] = True
        cnt = 0
        sum = 0
        while queue:
            x, y = queue.popleft()
            sum += population[x][y]
            cnt += 1
            population[x][y] = -1
            for i in range(4):
                nx = x + dx2[i]
                ny = y + dy2[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if (x, y) in borders and (nx, ny) in borders[(x, y)] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        return cnt, sum

    for b in borders:
        i, j = b[0], b[1]
        if not visited[i][j] and (i, j) in borders:
            cnt, total = bfs(i, j)
            value = total // cnt
            for a in range(n):
                for b in range(n):
                    if population[a][b] == -1:
                        population[a][b] = value
    days += 1

print(days)
