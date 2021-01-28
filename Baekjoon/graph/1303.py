from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())
soldiers = [list(stdin.readline().rstrip()) for _ in range(M)]
visited = [[0] * M for _ in range(N)]
queue = deque()

def bfs(x, y, c):
    queue.append((x, y))
    visited[x][y] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in (1,0), (-1,0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if soldiers[nx][ny] != c or visited[nx][ny] != 0:
                continue

            visited[nx][ny] = 1
            queue.append((nx, ny))
            cnt = cnt + 1
    return cnt

W_sum = 0
B_sum = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            value = bfs(i, j, soldiers[i][j])
            if soldiers[i][j] == 'W':
                W_sum += value ** 2
            else:
                B_sum += value ** 2
print(W_sum, B_sum)