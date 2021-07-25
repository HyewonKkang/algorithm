from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
area = []
M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]

def bfs(graph, i_, j_):
    visited[i_][j_] = 1
    cnt = 1
    queue = deque()
    queue.append((i_, j_))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny))
    return cnt

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and visited[i][j] == 0:
            cnt = bfs(graph, i, j)
            area.append(cnt)

area.sort()
print(len(area))
for i in area:
    print(i, end=' ')