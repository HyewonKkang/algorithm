# 포탑 부수기
from collections import deque
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
history = []
# attackedPaths = []


def findInHistory(i, j):
    h = history[::-1]
    return len(h) - h.index((i, j))


def find(attacker, isAttacker = True):
    tmp = []
    for i in range(n):
        for j in range(m):
            if not board[i][j]: continue
            if (i, j) == attacker: continue
            if (i, j) in history:
                tmp.append((board[i][j], findInHistory(i, j), i + j, j))
            else:
                tmp.append((board[i][j], -1, i + j, j))
    if isAttacker:
        return sorted(tmp, key=lambda x:(x[0], -x[1], -x[2], -x[3]))[0]
    return sorted(tmp, key=lambda x:(-x[0], x[1], x[2], x[3]))[0]


def laserAttack(x, y, attacked, path, visited):
    q = deque([(x, y, [(x, y)])])
    visited[x][y] = True
    while q:
        x, y, route = q.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = (x + dx) % n, (y + dy) % m
            if board[nx][ny] == 0 or visited[nx][ny]: continue

            if nx == attacked[0] and ny == attacked[1]:
                return route + [(nx, ny)]

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny, route + [(nx, ny)]))

    return []

def losePower(x, y, p):
    global board
    board[x][y] -= p
    if board[x][y] < 0: board[x][y] = 0


def bombAttack(attacker, attacked):
    res = []
    power = board[attacker[0]][attacker[1]]
    x, y = attacked
    losePower(x, y, power)

    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        nx, ny = x + dx, y + dy
        if nx < 0:
            nx = n - 1
        if nx >= n:
            nx = 0
        if ny < 0:
            ny = m - 1
        if ny >= m:
            ny = 0
        if (nx, ny) == attacker: continue

        if board[nx][ny]:
            losePower(nx, ny, power // 2)
            res.append((nx, ny))
    return res


def maintain(path):
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and (i, j) not in path:
                board[i][j] += 1


for _ in range(k):
    # 남은 포탑이 1개가 되면 중지
    if n * m - sum(board, []).count(0) <= 1:
        break

    # 공격자 선정
    tmp = find((-1, -1))
    attacker = (tmp[2] - tmp[3], tmp[3])
    board[attacker[0]][attacker[1]] += n + m
    history.append(attacker)

    # 공격할 포탑 선정
    tmp = find(attacker, False)
    attacked = (tmp[2] - tmp[3], tmp[3])

    # 공격
    visit = [[False] * m for _ in range(n)]
    visit[attacker[0]][attacker[1]] = 1
    laserPath = laserAttack(attacker[0], attacker[1], attacked, [], visit)
    if laserPath:
        power = board[attacker[0]][attacker[1]]
        losePower(attacked[0], attacked[1], power)
        maintain(laserPath)

        for loc in laserPath[1:-1]:
            if loc[0] == attacker[0] and loc[1] == attacker[1]: continue
            losePower(loc[0], loc[1], power // 2)
    else:
        path = bombAttack(attacker, attacked)
        maintain(path + [attacked] + [attacker])


print(max(sum(board, [])))

