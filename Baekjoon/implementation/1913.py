import sys
N = int(sys.stdin.readline())
find = int(sys.stdin.readline())
snails = [[0] * N for _ in range(N)]

x, y = N // 2, N // 2
snails[x][y] = 1
res_x, res_y = x, y

# 오 아래 아래 왼 왼 위 위
dx = [0, 1, 1, 0, 0, -1, -1]
dy = [1, 0, 0, -1, -1, 0, 0]

num = 2
k = 1
while num <= N ** 2:
    nx, ny = x - 1, y
    snails[nx][ny] = num
    x, y = nx, ny
    if num == find:
        res_x, res_y = nx, ny
    num += 1
    for i in range(7):
        tmp = 2 * k - 1 if i % 8 == 0 else k
        for j in range(tmp):
            nx = x + dx[i % 7]
            ny = y + dy[i % 7]
            snails[nx][ny] = num
            if num == find:
                res_x, res_y = nx, ny
            x, y = nx, ny
            num += 1
    k += 1

for i in range(N):
    for j in range(N):
        print(snails[i][j], end=' ')
    print()
print(res_x + 1, res_y + 1)