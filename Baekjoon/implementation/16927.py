import sys
import copy
input = sys.stdin.readline
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
circles = min(n, m) // 2


def printArray(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=' ')
        print()


def rotate(x_s, x_e, y_s, y_e, outer):
    copied = copy.deepcopy(arr)
    tmp = []
    for i in range(x_s, x_e):
        tmp.append(arr[i][y_s])
    for i in range(y_s, y_e):
        tmp.append(arr[x_e][i])
    for i in range(x_e, x_s, -1):
        tmp.append(arr[i][y_e])
    for i in range(y_e, y_s, -1):
        tmp.append(arr[x_s][i])

    new = [0] * outer
    for i in range(outer):
        new[(i + r) % outer] = tmp[i]

    idx = 0
    for i in range(x_s, x_e):
        copied[i][y_s] = new[idx]
        idx += 1
    for i in range(y_s, y_e):
        copied[x_e][i] = new[idx]
        idx += 1
    for i in range(x_e, x_s, -1):
        copied[i][y_e] = new[idx]
        idx += 1
    for i in range(y_e, y_s, -1):
        copied[x_s][i] = new[idx]
        idx += 1
    return copied


x_s, x_e, y_s, y_e = 0, n - 1, 0, m - 1
for c in range(circles):
    outer = 2 * (n - c * 2) + 2 * (m - 2 - c * 2)
    arr = rotate(x_s, x_e, y_s, y_e, outer)
    x_s += 1
    x_e -= 1
    y_s += 1
    y_e -= 1

printArray(arr)
