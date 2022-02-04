from collections import deque
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
res = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 1:
                    queue.append([nx, ny])
                    maze[nx][ny] = maze[x][y] + 1
    return maze[N - 1][M - 1]

print(bfs(0, 0))