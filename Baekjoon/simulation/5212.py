r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
disappeared = []


def find_path(x, y):
    cnt = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < r and 0 <= ny < c:
            if grid[nx][ny] == '.':
                cnt += 1
        else:
            cnt += 1
    if cnt == 3 or cnt == 4:
        disappeared.append((x, y))

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'X':
            find_path(i, j)

for (x, y) in disappeared:
    grid[x][y] = '.'

rows, cols = [], []
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'X':
            rows.append(i)
            cols.append(j)

if rows:
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            print(grid[i][j], end='')
        print()
else:
    print('X')
