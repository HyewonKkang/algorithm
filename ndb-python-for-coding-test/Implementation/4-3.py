loc = list(input())
loc[0] = int(chr(ord(loc[0]) - ord('1') + 1))
loc[1] = int(loc[1])
x, y = loc[0], loc[1]

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

cnt = 0
for i in range(8):
    nx = dx[i] + x
    ny = dy[i] + y
    if 0 < nx < 9 and 0 < ny < 9:
        cnt += 1
print(cnt)