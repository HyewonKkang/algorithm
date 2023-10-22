# 싸움땅
from collections import defaultdict
n, m, k = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    tmp = []
    for r in row:
        tmp.append([r])
    board.append(tmp)
players = [] # x, y, d, s, gun
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
points = [0] * m
playersTable = defaultdict(list)

for _ in range(m):
    x, y, d, s = map(int, input().split())
    players.append([x - 1, y - 1, d, s, 0])


def movePlayer(i):
    x, y, d, s, g = players[i]
    nx, ny = x + directions[d % 4][0], y + directions[d % 4][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        d += 2
        nx, ny = x + directions[d % 4][0], y + directions[d % 4][1]
    players[i] = [nx, ny, d, s, g]
    return nx, ny


def getMaxGun(x, y, cur):
    if not any(board[x][y]): return cur
    guns = board[x][y] + [cur] if cur else board[x][y]

    maxGun = max(guns)
    guns.remove(maxGun)
    board[x][y] = guns
    return maxGun


def moveLoser(i):
    x, y, d, s, g = players[i]
    nx, ny = x + directions[d % 4][0], y + directions[d % 4][1]
    while True:
        nx, ny = x + directions[d % 4][0], y + directions[d % 4][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or ((nx, ny) in playersTable and len(playersTable[(nx, ny)]) != 0):
            d += 1
        else:
            break
    g = getMaxGun(nx, ny, 0)
    # 진 플레이어는 PlayersTable 위치도 조정
    playersTable[(nx, ny)].append(i)
    players[i] = [nx, ny, d, s, g]


def afterFight(winner, loser, x, y):
    p1_skill, p1_gun = players[winner][3], players[winner][4]
    p2_skill, p2_gun = players[loser][3], players[loser][4]
    points[winner] += (p1_skill + p1_gun) - (p2_skill + p2_gun)

    if p2_gun: board[x][y].append(p2_gun)
    playersTable[(x, y)].remove(loser)
    moveLoser(loser)

    players[winner][4] = getMaxGun(x, y, players[winner][4])



def fight(p1, p2, x, y):
    p1_skill, p1_gun = players[p1][3], players[p1][4]
    p2_skill, p2_gun = players[p2][3], players[p2][4]
    if p1_skill + p1_gun > p2_skill + p2_gun:
        afterFight(p1, p2, x, y)
    elif p1_skill + p1_gun == p2_skill + p2_gun:
        if p1_skill > p2_skill:
            afterFight(p1, p2, x, y)
        else:
            afterFight(p2, p1, x, y)
    else:
        afterFight(p2, p1, x, y)

for round in range(k):
    playersTable = defaultdict(list)
    for i in range(m):
        x, y, a, b, c = players[i]
        playersTable[(x, y)].append(i)

    # 각 플레이어 한 칸 이동
    for i in range(m):
        x, y, a, b, c = players[i]
        nx, ny = movePlayer(i)
        playersTable[(x, y)].remove(i)
        playersTable[(nx, ny)].append(i)

        if len(playersTable[(nx, ny)]) == 1: # 해당 칸에 다른 플레이어가 없는 경우
            if any(board[nx][ny]):
                players[i][4] = getMaxGun(nx, ny, players[i][4])
        elif len(playersTable[(nx, ny)]) >= 2: # 해당 칸에 다른 플레이어가 있는 경우
            prev = playersTable[(nx, ny)][0]
            fight(i, prev, nx, ny)

print(*points)