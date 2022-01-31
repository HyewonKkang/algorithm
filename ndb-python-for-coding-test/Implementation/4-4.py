N, M = map(int, input().split())
x, y, direction = map(int, input().split())
maps = []
res = 1 # 방문한 칸의 수

for i in range(N):
    maps.append(list(map(int, input().split())))

# 북, 서, 남, 동 (0, 1, 2, 3)
ways = [0, 1, 2, 3]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

tmp = 0
while True:
    direction = (direction + 1) % 4
    nx = dx[direction] + x
    ny = dy[direction] + y

    if maps[nx][ny] == 1:
        tmp += 1
        if tmp == 4:
            nx2 = dx[direction - 2] + x
            ny2 = dy[direction - 2] + y
            if maps[nx2][ny2] == 1:
                break
            x, y = nx2, ny2
        continue
    tmp = 0
    maps[x][y] = 1
    x, y = nx, ny
    res += 1

print(res)