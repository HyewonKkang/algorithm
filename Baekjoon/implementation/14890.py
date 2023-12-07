n, l = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
answer = 0
columns = []
for j in range(n):
    tmp = []
    for i in range(n):
        tmp.append(maps[i][j])
    columns.append(tmp)
ways = [row for row in maps] + columns

def getCounter(arr):
    tmp = []
    counts = 0
    prev = arr[0]
    for num in arr:
        if prev == num:
            counts += 1
        else:
            tmp.append((prev, counts))
            prev = num
            counts = 1
    tmp.append((num, counts))
    return tmp


def checkAvailable(arr):
    tmp = getCounter(arr)
    checked = [False] * n

    index = tmp[0][1]
    prev = tmp[0]
    for info in tmp[1:]:
        if abs(prev[0] - info[0]) > 1: return False
        height, counts = info
        if prev[0] < height:
            if prev[1] < l:
                return False
            for c in range(l):
                if checked[index - 1 - c]: return False
                checked[index - 1 - c] = True
        else:
            if counts < l:
                return False
            for c in range(l):
                if checked[index + c]: return False
                checked[index + c] = True
        prev = info
        index += counts
    return True


for way in ways:
    answer += checkAvailable(way)

print(answer)