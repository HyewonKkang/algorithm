N = int(input())
plans = list(input().split())
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
directions = ['R', 'L', 'U', 'D']

for p in plans:
    for i in range(4):
        if p == directions[i]:
            nx = dx[i] + x
            ny = dy[i] + y
            break
    if 0 < nx < N + 1 and 0 < ny < N + 1:
        x, y = nx, ny
print(x, y)

