from collections import deque
m, n, h = map(int, input().split())
storage = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
tomatoes = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if storage[i][j][k] == 1:
                tomatoes.append((i, j, k))
answer = 0

def isDone():
    return

def ripe(tomato):
    x, y, z = tomato
    for dx, dy, dz in [(0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]:
        nx, ny, nz = x + dx, y + dy, z + dz
        if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
            continue
        if storage[nx][ny][nz] == 0:
            storage[nx][ny][nz] = 1
            tmp.append((nx, ny, nz))


while tomatoes:
    tmp = []
    for _ in range(len(tomatoes)):
        tomato = tomatoes.popleft()
        ripe(tomato)

    tomatoes = deque(tmp)
    if tmp: answer += 1

flag = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if storage[i][j][k] == 0:
                flag = False

print(answer if flag else -1)