puzzles = [list(map(int, list(input()))) for _ in range((9))]
zeros = []

def row_check(r, n):
    for i in range(9):
        if puzzles[r][i] == n:
            return False
    return True

def col_check(c, n):
    for i in range(9):
        if puzzles[i][c] == n:
            return False
    return True

def square_check(r, c, n):
    nr, nc = (r // 3) * 3, (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzles[nr + i][nc + j] == n:
                return False
    return True

def print_sudoko():
    for row in puzzles:
        str_nums = list(map(str, row))
        print(''.join(str_nums))
    print()


def check(i, j, num):
    return row_check(i, num) and col_check(j, num) and square_check(i, j, num)


def dfs(idx):
    if idx == len(zeros):
        print_sudoko()
        exit()
    r, c = zeros[idx]
    for num in range(1, 10):
        if check(r, c, num):
            puzzles[r][c] = num
            dfs(idx + 1)
            puzzles[r][c] = 0



for i in range(9):
    for j in range(9):
        if not puzzles[i][j]:
            zeros.append((i, j))
dfs(0)