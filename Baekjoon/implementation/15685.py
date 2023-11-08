n = int(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
grid = [[False] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    grid[x][y] = True

    curves = [d]
    for _ in range(g):
        for i in range(len(curves) - 1, -1, -1):
            curves.append((curves[i] + 1) % 4)

    for c in curves:
        x, y = x + dx[c], y + dy[c]
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue
        grid[x][y] = True

answer = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]:
            answer += 1
print(answer)
