n = int(input())
area = []
teachers = 0
answer = False

for _ in range(n):
    row = list(input().split())
    teachers += row.count('T')
    area.append(row)

def check(area, x, y):
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        while True:
            if nx < 0 or nx >= n or ny < 0 or ny >= n: break
            if area[nx][ny] == 'O': break
            if area[nx][ny] == 'S':
                return False
            nx += dx
            ny += dy
    return True


def backtracking(area, barriers):
    global answer

    if barriers == 3:
        cnt = 0
        for i in range(n):
            for j in range(n):
                if area[i][j] == 'T':
                    if not check(area, i, j):
                        return
                    cnt += 1

        if cnt == teachers:
            answer = True
        return

    for i in range(n):
        for j in range(n):
            if area[i][j] == 'X':
                area[i][j] = 'O'
                backtracking(area, barriers + 1)
                area[i][j] = 'X'




backtracking(area, 0)
print('YES' if answer else 'NO')