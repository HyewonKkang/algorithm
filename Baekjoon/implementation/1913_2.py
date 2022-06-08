import sys
n = int(sys.stdin.readline())
find = int(sys.stdin.readline())
snails = [[0] * n for _ in range(n)]
answer = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dr = [0, 1, 0, -1] # 오른쪽, 아래쪽, 왼쪽, 위쪽 순서
dc = [1, 0, -1, 0]

r = n // 2
c = n // 2
num = 1
len = 0

snails[r][c] = num
if find == 1: answer = [r + 1, c + 1]

while True:
    for i in range(4):
        for _ in range(len):
            r += dr[i]
            c += dc[i]
            num += 1
            snails[r][c] = num
            if num == find:
                answer = [r + 1, c + 1]

    if r == c == 0:
        break
    r -= 1
    c -= 1
    len += 2

for i in range(n):
    print(*snails[i])
print(*answer)
