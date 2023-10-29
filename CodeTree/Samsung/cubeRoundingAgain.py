# 정육면체 한번 더 굴리기
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dice = [1, 2, 3, 6, 5, 4] # 위, 앞, 오, 아래, 뒤, 왼
roll_direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오, 아래, 왼, 위
dice_dir = 0
dice_pos = (0, 0)
score_table = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def createScoreTable(cur_x, cur_y, num):
    tmp = [(cur_x, cur_y)]
    q = deque([(cur_x, cur_y)])
    visited[cur_x][cur_y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if board[nx][ny] == num and not visited[nx][ny]:
                q.append((nx, ny))
                tmp.append((nx, ny))
                count += 1
                visited[nx][ny] = True
    for pos in tmp:
        x, y = pos
        score_table[x][y] = count * num


def rollDice(d):
    global dice
    tmp = dice[:]
    d = d % 4
    if d == 0:
        dice = [tmp[5], tmp[1], tmp[0], tmp[2], tmp[4], tmp[3]]
    elif d == 1:
        dice = [tmp[4], tmp[0], tmp[2], tmp[1], tmp[3], tmp[5]]
    elif d == 2:
        dice = [tmp[2], tmp[1], tmp[3], tmp[5], tmp[4], tmp[0]]
    elif d == 3:
        dice = [tmp[1], tmp[3], tmp[2], tmp[4], tmp[0], tmp[5]]

def moveDice():
    global dice_pos, dice_dir
    x, y = dice_pos
    dx, dy = roll_direction[dice_dir % 4]
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n:
        dice_pos = (nx, ny)
        return
    else:
        dice_dir += 2
        moveDice()


# score table 생성
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            createScoreTable(i, j, board[i][j])

# 주사위 굴리기
for _ in range(m):
    moveDice()
    rollDice(dice_dir)

    x, y = dice_pos
    answer += score_table[x][y]

    if dice[3] > board[x][y]:
        dice_dir += 1
    elif dice[3] < board[x][y]:
        dice_dir -= 1


print(answer)