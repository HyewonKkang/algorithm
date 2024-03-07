area = [list(map(int, input().split())) for _ in range(10)]
answer = int(1e9)


def isCover(arr, sx, sy, size):
    for x in range(sx, sx + size):
        for y in range(sy, sy + size):
            if arr[x][y] == 0:
                return False
    return True


def cover(arr, sx, sy, size):
    tmp = [row[:] for row in arr]
    for x in range(sx, sx + size):
        for y in range(sy, sy + size):
            tmp[x][y] = 0
    return tmp


def checkCount(dic):
    for i in range(1, 6):
        if dic[i] > 5: return False
    return True


def isDone(arr):
    for x in range(10):
        for y in range(10):
            if arr[x][y] == 1:
                return False
    return True


def backtracking(arr, count, sx):
    global answer
    if not checkCount(count):
        return

    if isDone(arr):
        answer = min(answer, sum(count.values()))
        return

    for i in range(sx, 10):
        for j in range(10):
            if arr[i][j] == 1:
                for size in range(1, 6):
                    if count[size] == 5: continue
                    mi, mj = i + size - 1, j + size - 1
                    if mi < 0 or mi >= 10 or mj < 0 or mj >= 10: continue
                    if isCover(arr, i, j, size):
                        count[size] += 1
                        tmp = cover(arr, i, j, size)
                        backtracking(tmp, count, i)
                        count[size] -= 1
                return


backtracking(area, {i:0 for i in range(1, 6)}, 0)
print(answer if answer != int(1e9) else -1)