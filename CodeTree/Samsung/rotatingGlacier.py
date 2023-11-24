# 회전하는 빙하
from collections import deque
n, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2 ** n)]
rotations = list(map(int, input().split()))
length = len(grid)

def divideGlaciers(lv):
    size = 2 ** lv
    result = []
    idxs = []
    size_ = 2 ** (lv - 1)
    for i in range(0, length, size):
        for j in range(0, length, size):
            outer = []
            inner = []
            for a in range(i, i + size_):
                for b in range(j, j + size_):
                    inner.append(grid[a][b])
            outer.append(inner)
            inner = []
            for a in range(i, i + size_):
                for b in range(j + size_, j + size):
                    inner.append(grid[a][b])
            outer.append(inner)
            inner = []
            for a in range(i + size_, i + size):
                for b in range(j, j + size_):
                    inner.append(grid[a][b])
            outer.append(inner)
            inner = []
            for a in range(i + size_, i + size):
                for b in range(j + size_, j + size):
                    inner.append(grid[a][b])
            outer.append(inner)
            result.append(outer)
            idxs.append((i, j))
    return result, idxs

def rotate(arr):
    blocks = [row[:] for row in arr]
    if len(blocks) >= 4:
        blocks[0], blocks[1], blocks[2], blocks[3] = blocks[2], blocks[0], blocks[3], blocks[1]
    return sum(blocks, [])


def putGlaciers(arr, idx, lv):
    global grid
    sx, sy = idx
    size = 2 ** lv
    k = 0
    size_ = 2 ** (lv - 1)
    for a in range(sx, sx + size_):
        for b in range(sy, sy + size_):
            grid[a][b] = arr[k]
            k += 1
    for a in range(sx, sx + size_):
        for b in range(sy + size_, sy + size):
            grid[a][b] = arr[k]
            k += 1
    for a in range(sx + size_, sx + size):
        for b in range(sy, sy + size_):
            grid[a][b] = arr[k]
            k += 1
    for a in range(sx + size_, sx + size):
        for b in range(sy + size_, sy + size):
            grid[a][b] = arr[k]
            k += 1

def melt():
    global grid
    tmp = [row[:] for row in grid]

    for x in range(length):
        for y in range(length):
            count = 0
            if grid[x][y] <= 0: continue
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= length or ny < 0 or ny >= length: continue
                if grid[nx][ny] > 0:
                    count += 1
            if count < 3:
                tmp[x][y] -= 1
    grid = [row[:] for row in tmp]


def getGlacierSize(x, y):
    global visited
    q = deque([(x, y)])
    visited[x][y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= length or ny < 0 or ny >= length: continue
            if grid[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                count += 1
                q.append((nx, ny))
    return count

for level in rotations:
    if level >= 1:
        glaciers, idxs = divideGlaciers(level)
        for idx, glacier in zip(idxs, glaciers):
            rotated = rotate(glacier)
            putGlaciers(rotated, idx, level)

    melt()

print(sum(sum(grid, [])))
maxSize = 0
visited = [[False] * length for _ in range(length)]
for i in range(length):
    for j in range(length):
        if not visited[i][j] and grid[i][j] > 0:
            maxSize = max(maxSize, getGlacierSize(i, j))
print(maxSize)
