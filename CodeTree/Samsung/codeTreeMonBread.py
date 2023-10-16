# 코드트리 빵
from collections import deque
n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
stores = [(-1, -1)]
basecamps = []
people = [0] + [(-1, -1) for _ in range(m)]
arrived = [True] + [False] * m
time = 1

for i in range(n):
    for j in range(n):
        if area[i][j]:
            basecamps.append((i, j))

for _ in range(m):
    x, y = map(int, input().split())
    stores.append((x - 1, y - 1))


def getShortestPath(src, dst):
    x, y = src
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    q = deque([(x, y, [(x, y)])])

    while q:
        x, y, path = q.popleft()
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) == dst:
                return path + [(nx, ny)]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] or area[nx][ny] == -1:
                continue
            q.append((nx, ny, path + [(nx, ny)]))
            visited[nx][ny] = True
    return []


def findBasecamp(person_idx):
    store = stores[person_idx]
    distance = int(1e9)
    result = []

    for basecamp in basecamps:
        if area[basecamp[0]][basecamp[1]] == -1: continue

        route = getShortestPath(basecamp, store)
        if not route: continue
        if len(route) == distance:
            result.append(route[0])
        elif len(route) < distance:
            result = [route[0]]
            distance = len(route)
    result.sort()
    return result[0]


def move(idx):
    global people
    route = getShortestPath(people[idx], stores[idx])
    nx, ny = route[1]
    people[idx] = (nx, ny)


while True:
    if all(arrived[1:]): break
    # 격자에 있는 사람들 모두 이동
    for i in range(1, time):
        if i > m: break
        if not arrived[i]:
            move(i)

    # 편의점에 사람이 도달한 경우 멈춤 -> 해당 칸 -1 처리
    for i in range(1, time):
        if i > m: break
        if arrived[i]: continue
        if people[i] == stores[i]:
            x, y = stores[i]
            area[x][y] = -1
            arrived[i] = True

    # 베이스캠프로 도달
    if time <= m:
        basecamp = findBasecamp(time)
        area[basecamp[0]][basecamp[1]] = -1
        people[time] = (basecamp[0], basecamp[1])

    time += 1




print(time - 1)