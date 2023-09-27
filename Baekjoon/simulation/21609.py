from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0
def findBlockGroup(x, y, color, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    count = 1
    rainbow = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and (grid[nx][ny] == color or grid[nx][ny] == 0):
                visited[nx][ny] = True
                count += 1
                if grid[nx][ny] == 0: rainbow += 1
                q.append((nx, ny))
    return rainbow, count

def resetVisited(v):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0 and v[i][j]:
                v[i][j] = False
    return v


def removeLargestGroup(x, y, color):
    visited = [[False] * n for _ in range(n)]
    q = deque([(x, y)])
    grid[x][y] = -2
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and (grid[nx][ny] == color or grid[nx][ny] == 0):
                visited[nx][ny] = True
                grid[nx][ny] = -2
                q.append((nx, ny))


def hasGravity():
    for j in range(n):
        col = [-2] * n
        tmp_colors = []
        for i in range(n):
            if grid[i][j] != -1 and grid[i][j] != -2:
                tmp_colors.append(grid[i][j])
            if grid[i][j] == -1:
                col[i] = -1
                for k in range(len(tmp_colors)):
                    col[i - k - 1] = tmp_colors[len(tmp_colors) - 1 - k]
                tmp_colors = []
        k = n - 1
        for i in range(len(tmp_colors) - 1, -1, -1):
            col[k] = tmp_colors[i]
            k -= 1

        for k in range(n):
            grid[k][j] = col[k]

def rotate():
    tmp = []

    for j in range(n - 1, -1, -1):
        for i in range(n):
            tmp.append(grid[i][j])

    k = 0
    for i in range(n):
        for j in range(n):
            grid[i][j] = tmp[k]
            k += 1



while True:
    largestGroup = (0, 0, 0, 0) # 블록 개수, 무지개 개수, 행, 열
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] > 0:
                rainbow, count = findBlockGroup(i, j, grid[i][j], visited)
                largestGroup = max(largestGroup, (count, rainbow, i, j))
                visited = resetVisited(visited)
    if largestGroup[0] < 2: break
    if largestGroup == (0, 0, 0, 0): break
    removeLargestGroup(largestGroup[2], largestGroup[3], grid[largestGroup[2]][largestGroup[3]])
    answer += largestGroup[0] ** 2
    hasGravity()
    rotate()
    hasGravity()

print(answer)
