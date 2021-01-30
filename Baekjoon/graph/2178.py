from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
maze = []
visited = [[0] * M for _ in range(N)]

#  좌/우/아래/
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    line = list(map(int, stdin.readline().rstrip()))
    maze.append(line)


def bfs(maze):
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and maze[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

print(bfs(maze))
