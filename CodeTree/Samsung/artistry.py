# 예술성
from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def createGroup(x, y, visited, number):
    q = deque([(x, y)])
    color = board[x][y]
    visited[x][y] = number
    neighbors = {i:0 for i in range(1, number)}
    count = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if not visited[nx][ny] and board[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = number
                count += 1
            elif visited[nx][ny] != 0 and visited[nx][ny] != number:
                neighbors[visited[nx][ny]] += 1


    return (color, count, neighbors), visited

def divideGroups():
    checked = [[0] * n for _ in range(n)]
    groups = []
    groupNumber = 1

    for i in range(n):
        for j in range(n):
            if not checked[i][j]:
                group, checked = createGroup(i, j, checked, groupNumber)
                groupNumber += 1
                groups.append(group)
    return groups



def getArtisticScore(groups):
    result = 0
    groups = [0] + groups
    counts = len(groups)
    for i in range(1, counts):
        for j in range(i + 1, counts):
            if i == j: continue
            a_number, a_counts, prev_combs = groups[i]
            b_number, b_counts, combs = groups[j]
            comb = combs[i]
            if comb == 0: continue
            result += (a_counts + b_counts) * a_number * b_number * comb
    return result



def rotateSquare(xs, xe, ys, ye):
    global board
    tmp = []
    for i in range(xs, xe):
        row = []
        for j in range(ys, ye):
            row.append(board[i][j])
        tmp.append(row)
    rotated = list(map(list, zip(*tmp[::-1])))
    for i in range(xs, xe):
        for j in range(ys, ye):
            board[i][j] = rotated[i - xs][j - ys]


def rotateCross():
    global board
    centerLine = list(map(list, zip(*board)))[n // 2]
    center = [board[n // 2][n // 2]]
    rows = deque([board[n // 2][:n // 2][::-1], centerLine[:n // 2][::-1], board[n // 2][n // 2 + 1:], centerLine[n // 2 + 1:]])
    rows.rotate(-1)
    hor, ver = rows[0][::-1] + center + rows[2], rows[1][::-1] + center + rows[3]

    for i in range(n):
        board[n // 2][i] = hor[i]
    for i in range(n):
        board[i][n // 2] = ver[i]




def rotate():
    # 십자 모양 회전
    rotateCross()

    # 외부 회전
    for xs, xe, ys, ye in [(0, n // 2, 0, n // 2), (0, n // 2, n // 2 + 1, n), (n // 2 + 1, n, 0, n // 2), (n // 2 + 1, n, n // 2 + 1, n)]:
        rotateSquare(xs, xe, ys, ye)


for i in range(4):
    groups = divideGroups()
    answer += getArtisticScore(groups)

    if i < 3:
        rotate()

print(answer)