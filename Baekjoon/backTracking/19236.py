import copy
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
area = [] # (물고기 번호, 방향)
fish = []

answer = 0
for _ in range(4):
    row = list(map(int, input().split()))
    tmp = []
    for i in range(0, 8, 2):
        tmp.append((row[i], row[i + 1]))
        fish.append(row[i])
    area.append(tmp)

fish.sort()

def sharkMoves(shark, dir, arr):
    result = []
    x, y = shark[0], shark[1]
    dx, dy = directions[dir - 1]
    while True:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            break
        if arr[nx][ny] != (-1, -1):
            result.append((nx, ny))
        x, y = nx, ny
    return result

def getTotal(killed):
    total = 0
    for i in range(16):
        if killed[i]:
            total += fish[i]
    return total

def getFishLoc(fishNum, arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == fishNum:
                return (i, j)
    return (-1, -1)


def fishMoves(arr, killed, shark):
    for i, f in enumerate(fish):
        if killed[i]: continue
        x, y = getFishLoc(f, arr)
        dir = arr[x][y][1]
        for _ in range(8):
            dx, dy = directions[dir - 1]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx == shark[0] and ny == shark[1]):
                dir = (dir + 1) % 8
            else:
                break
        if arr[nx][ny] == -1:
            arr[nx][ny] = (arr[x][y][0], dir)
            arr[x][y] = (-1, -1)
        else:
            tmp = arr[nx][ny]
            arr[nx][ny] = (arr[x][y][0], dir)
            arr[x][y] = tmp
    return arr


def simulation(shark, shark_dir, killed, arr):
    global answer

    tmp = copy.deepcopy(arr)
    arr = fishMoves(tmp, killed, shark)
    nextSharkLocs = sharkMoves(shark, shark_dir, arr)

    if not nextSharkLocs:
        answer = max(answer, getTotal(killed))
        return

    for loc in nextSharkLocs:
        x, y = loc
        prev = arr[x][y]
        if arr[x][y] == (-1, -1): continue

        killed[fish.index(arr[x][y][0])] = True
        arr[x][y] = (-1, -1)
        simulation((x, y), prev[1], killed, arr)
        killed[fish.index(prev[0])] = False
        arr[x][y] = prev


shark_loc = (0, 0)
shark_dir = area[0][0][1]
killed = [False] * 16
killed[fish.index(area[0][0][0])] = True
area[0][0] = (-1, -1)
simulation(shark_loc, shark_dir, killed, area)
print(answer)