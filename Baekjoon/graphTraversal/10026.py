from collections import deque
n = int(input())
painting = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
a, b = 0, 0


def bfs(x, y, color, compare_method):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= n or visited[nx][ny]:
                continue
            if compare_method(painting[nx][ny], color):
                visited[nx][ny] = True
                q.append((nx, ny))

def isSameColor(c1, c2):
    return c1 == c2

def isWeaknessSameColor(c1, c2):
    if c1 == c2:
        return True
    if c2 == 'G' and c1 == 'R':
        return True
    if c2 == 'R' and c1 == 'G':
        return True


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, painting[i][j], isSameColor)
            a += 1

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, painting[i][j], isWeaknessSameColor)
            b += 1
print(a, b)