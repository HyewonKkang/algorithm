from collections import deque
import sys
input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
animals = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'v' or arr[i][j] == 'k':
            animals.append((i, j))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = [0, 0] # v, k

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    res = [0, 0]
    if arr[x][y] == 'v':
        res[0] += 1
    elif arr[x][y] == 'k':
        res[1] += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and arr[nx][ny] != '#':
                    visited[nx][ny] = True
                    if arr[nx][ny] == 'v':
                        res[0] += 1
                    elif arr[nx][ny] == 'k':
                        res[1] += 1
                    q.append([nx, ny])
    return res

for a in animals:
    if not visited[a[0]][a[1]]:
        tmp = bfs(a[0], a[1])
        if tmp[0] >= tmp[1]:
            cnt[0] += tmp[0]
        else:
            cnt[1] += tmp[1]


print(cnt[1], cnt[0])