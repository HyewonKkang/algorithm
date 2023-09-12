import copy
n, m = map(int, input().split())
cctvs = []
area = []
answer = int(1e9)

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if 1 <= row[j] <= 5:
            cctvs.append((row[j], i, j))
    area.append(row)

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

def monitor(dir_set, x, y, arr):
    for dx, dy in dir_set:
        _x, _y = x, y
        while True:
            nx, ny = _x + dx, _y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] == 6:
                break
            if arr[nx][ny] == 0:
                arr[nx][ny] = -1
            _x, _y = nx, ny

    return arr

def backtracking(depth, arr):
    global answer
    if depth == len(cctvs):
        counts = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    counts += 1
        answer = min(answer, counts)
        return
    cctv_type, x, y = cctvs[depth]

    tmp = copy.deepcopy(arr)
    for dir_set in getDirections(cctv_type):
        tmp = monitor(dir_set, x, y, tmp)
        backtracking(depth + 1, tmp)
        tmp = copy.deepcopy(arr)


backtracking(0, area)
print(answer)