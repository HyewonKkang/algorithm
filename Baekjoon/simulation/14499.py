n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [0, 0, 0, 0, 0, 0] # 왼, 앞, 오, 뒤, 위, 아래

def rollDice(d):
    global dice
    tmp = dice[:]
    if d == 1: # 동
        tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5] = dice[5], dice[1], dice[4], dice[3], dice[0], dice[2]
    elif d == 2: # 서
        tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5] = dice[4], dice[1], dice[5], dice[3], dice[2], dice[0]
    elif d == 3: # 북
        tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5] = dice[0], dice[5], dice[2], dice[4], dice[1], dice[3]
    elif d == 4: # 남
        tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5] = dice[0], dice[4], dice[2], dice[5], dice[3], dice[1]
    dice = tmp[:]

for command in commands:
    dir = directions[command - 1]
    nx, ny = x + dir[0], y + dir[1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
    rollDice(command)
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[5]
    else:
        dice[5] = maps[nx][ny]
        maps[nx][ny] = 0
    print(dice[4])
    x, y = nx, ny