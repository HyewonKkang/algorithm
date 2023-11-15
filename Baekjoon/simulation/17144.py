r, c, t = map(int, input().split())
amount = [list(map(int, input().split())) for _ in range (r)]
cleaner = [row[0] for row in amount].index(-1)

def spread(x, y, added):
    count = 0
    for dx, dy in (0, -1), (1, 0), (-1, 0), (0, 1):
        nx, ny = dx + x, dy + y
        if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
        if amount[nx][ny] >= 0:
            added[nx][ny] += amount[x][y] // 5
            count += 1
    amount[x][y] -= (amount[x][y] // 5) * count
    return added

def activate(dx, dy, start):
    direction = 0
    prev = 0
    x, y = start
    while True:
        nx, ny = x + dx[direction], y + dy[direction]
        if x == start[0] and y == 0: break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direction += 1
            continue
        amount[x][y], prev = prev, amount[x][y]
        x, y = nx, ny

for _ in range(t):
    added = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if amount[i][j] > 0:
                added = spread(i, j, added)
    amount = [[amount[i][j] + added[i][j] for j in range(c)] for i in range(r)]
    activate([0, -1, 0, 1], [1, 0, -1, 0], (cleaner, 1))
    activate([0, 1, 0, -1], [1, 0, -1, 0], (cleaner + 1, 1))

print(sum(sum(row) for row in amount) + 2)