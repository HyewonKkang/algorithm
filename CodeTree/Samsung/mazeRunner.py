# 메이즈 러너
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
members = []
for _ in range(m):
    info = list(map(int, input().split()))
    members.append((info[0] - 1, info[1] - 1))
exit = tuple(map(int, input().split()))
exit = (exit[0] - 1, exit[1] - 1)
time = 0
answer = 0

def getDistanceTable():
    table = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            table[i][j] = getDistance(i, j, exit[0], exit[1])
    return table


def getDistance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def go(x, y, distance_table):
    global answer
    exit_distance = distance_table[x][y]
    result = tuple()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        if 0 <= distance_table[nx][ny] < exit_distance and maze[nx][ny] == 0:
            result = (nx, ny)
            break
    else:
        return x, y
    answer += 1
    return result[0], result[1]


def findSquareStart(x1, y1, x2, y2):
    side_length = max(abs(x2 - x1), abs(y2 - y1))
    start_x, start_y = max(x1, x2) - side_length, max(y1, y2) - side_length
    if start_x < 0: start_x = 0
    if start_y < 0: start_y = 0
    return (side_length, start_x, start_y)


def rotate(side_length, square_start):
    global exit
    square = []
    sx, sy = square_start

    if sx <= exit[0] <= sx + side_length and sy <= exit[1] <= sy + side_length:
        maze[exit[0]][exit[1]] = -1

    for i in range(sx, sx + side_length + 1):
        tmp = []
        for j in range(sy, sy + side_length + 1):
            tmp.append(maze[i][j] if maze[i][j] <= 0 else maze[i][j] - 1)
        square.append(tmp)

    # 회전
    rotated = list(map(list, zip(*square[::-1])))
    for i in range(sx, sx + side_length + 1):
        for j in range(sy, sy + side_length + 1):
            new_val = rotated[i - sx][j - sy]
            if new_val == -1:
                maze[i][j] = 0
                exit = (i, j)
            else:
                maze[i][j] = new_val
    # 멤버 회전
    members_square = [[[] for _ in range(side_length + 1)] for _ in range(side_length + 1)]
    for i, member in enumerate(members):
        mx, my = member
        if sx <= mx <= sx + side_length and sy <= my <= sy + side_length:
            members_square[mx - sx][my - sy].append(i)
    rotated_members = list(map(list, zip(*members_square[::-1])))
    for i in range(side_length + 1):
        for j in range(side_length + 1):
            if rotated_members[i][j]:
                for idx in rotated_members[i][j]:
                    members[idx] = (sx + i, sy + j)

while time < k and members:
    # 참가자 이동
    distance_table = getDistanceTable()
    removed = []
    for i, (x, y) in enumerate(members):
        nx, ny = go(x, y, distance_table)
        members[i] = (nx, ny)
        if nx == exit[0] and ny == exit[1]:
            removed.append(i)

    removed.reverse()
    for r in removed:
        del members[r]
    if not members: break

    # 미로 회전
    tmp = []
    for member in members:
        x, y = member
        tmp.append(findSquareStart(x, y, exit[0], exit[1]))
    tmp.sort()
    side_length, x, y = tmp[0]
    rotate(side_length, (x, y))
    time += 1

print(answer)
print(exit[0] + 1, exit[1] + 1)