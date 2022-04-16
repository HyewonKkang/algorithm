import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def rotate(x_s, x_e, y_s, y_e):
    circles = min(n, m) // 2
    a = [[0] * m for _ in range(n)]
    for c in range(circles):
        for i in range(x_s, x_e):
            a[i + 1][y_s] = arr[i][y_s]
        for i in range(y_s, y_e):
            a[x_e][i + 1] = arr[x_e][i]
        for i in range(x_e, x_s, -1):
            a[i - 1][y_e] = arr[i][y_e]
        for i in range(y_e, y_s, -1):
            a[x_s][i - 1] = arr[x_s][i]
        x_e -= 1
        y_e -= 1
        x_s += 1
        y_s += 1

    return a

for i in range(r):
    arr = rotate(0, n - 1, 0, m - 1)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()