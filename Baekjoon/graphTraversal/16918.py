import sys
from collections import deque
R, C, N = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
res = []

def fill():
    res = [['O'] * C for _ in range(R)]
    return res

def find_loc():
    res = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                res.append((i, j))
                grid[i][j] = '.'
            else:
                grid[i][j] = 'O'
    return res

def bomb():
    q = deque(find_loc())
    while q:
        x, y = q.popleft()
        grid[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                grid[nx][ny] = '.'

def print_arr(res):
    for i in range(R):
        for j in range(C):
            print(res[i][j], end = '')
        print()


if N <= 1:
    print_arr(grid)
elif N % 2 == 0:
    res = fill()
    print_arr(res)
elif N % 4 == 1:
    bomb()
    bomb()
    print_arr(grid)
elif N % 4 == 3:
    bomb()
    print_arr(grid)
