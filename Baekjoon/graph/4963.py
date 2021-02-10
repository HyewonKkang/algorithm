from collections import deque
while True:
    w, h = map(int, input().split())
    cnt = 0
    if w == 0 and h == 0:
        break
    graph = []
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    queue = deque()

    for _ in range(h):
        line = list(map(int, input().split()))
        graph.append(line)

    visited = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = 1
                cnt += 1

                while queue:
                    x, y = queue.popleft()

                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < h and 0 <= ny < w:
                            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                                visited[nx][ny] = 1
                                queue.append((nx, ny))
    print(cnt)
