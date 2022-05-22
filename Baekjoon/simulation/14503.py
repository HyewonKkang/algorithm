import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 북:0, 서:1, 남:2, 동:3
r_x, r_y, r_d = map(int, input().split())
if r_d == 1: r_d = 3
elif r_d == 3: r_d = 1
arr = [list(map(int, input().split())) for _ in range(n)]
cleaned = [[False] * m for _ in range(n)]
a_cnt = 0

while True:
    cleaned[r_x][r_y] = True
    if a_cnt == 4:
        a_cnt = 0
        tmp_x = r_x + dx[(r_d + 2) % 4]
        tmp_y = r_y + dy[(r_d + 2) % 4]
        if 0 <= tmp_x < n and 0 <= tmp_y < m:
            if arr[tmp_x][tmp_y] == 0:
                r_x, r_y = tmp_x, tmp_y
            else:
                break

    tmp_x = r_x + dx[(r_d + 1) % 4]
    tmp_y = r_y + dy[(r_d + 1) % 4]
    if 0 <= tmp_x < n and 0 <= tmp_y < m and arr[tmp_x][tmp_y] == 0 and not cleaned[tmp_x][tmp_y]:
            r_d += 1
            r_x += dx[r_d % 4]
            r_y += dy[r_d % 4]
            a_cnt = 0
    else:
        r_d += 1
        a_cnt += 1

res = 0
for i in range(n):
    for j in range(m):
        if cleaned[i][j]:
            res += 1
print(res)