from itertools import product
n, m = map(int, input().split())
cctvs = []
area = []
answer = int(1e9)

def getDirections(cctv):
    if cctv == 1:
        return [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]]
    elif cctv == 2:
        return [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
    elif cctv == 3:
        return [[(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)]]
    elif cctv == 4:
        return [[(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)], [(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)]]
    elif cctv == 5:
        return [[(0, 1), (1, 0), (-1, 0), (0, -1)]]

def monitor(dir_set, x, y, visited):
    for dx, dy in dir_set:
        _x, _y = x, y
        while True:
            nx, ny = _x + dx, _y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or area[nx][ny] == 6:
                break
            if not visited[nx][ny]:
                visited[nx][ny] = True
            _x, _y = nx, ny

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if 1 <= row[j] <= 5:
            cctvs.append((row[j], i, j))
    area.append(row)

dirs = [getDirections(cctv[0]) for cctv in cctvs]
for dirs_set in list(product(*dirs)):
    tmp = 0
    visited = [[False] * m for _ in range(n)]
    for i, dir_set in enumerate(dirs_set):
        monitor(dir_set, cctvs[i][1], cctvs[i][2], visited)

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and area[i][j] == 0:
                tmp += 1
    answer = min(answer, tmp)
print(answer)