n, m, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
operations = list(map(int, input().split()))

def flip(arr, isVertical):
    return arr[::-1] if isVertical else [row[::-1] for row in arr]

def rotate(arr, isClockwise):
    rotated = []
    n, m = len(arr), len(arr[0])
    if isClockwise:
        for i in range(m):
            tmp = []
            for j in range(n - 1, -1, -1):
                tmp.append(arr[j][i])
            rotated.append(tmp)
    else:
        for i in range(m - 1, -1, -1):
            tmp = []
            for j in range(n):
                tmp.append(arr[j][i])
            rotated.append(tmp)
    return rotated

def move(arr, isForwarded):
    n, m = len(arr), len(arr[0])
    n_mid, m_mid = n // 2, m // 2
    g1 = [row[:m_mid] for row in arr[:n_mid]]
    g2 = [row[m_mid:] for row in arr[:n_mid]]
    g3 = [row[:m_mid] for row in arr[n_mid:]]
    g4 = [row[m_mid:] for row in arr[n_mid:]]
    if isForwarded:
        arr[:n_mid] = [g3[i] + g1[i] for i in range(n_mid)]
        arr[n_mid:] = [g4[i] + g2[i] for i in range(n_mid)]
    else:
        arr[:n_mid] = [g2[i] + g4[i] for i in range(n_mid)]
        arr[n_mid:] = [g1[i] + g3[i] for i in range(n_mid)]
    return arr

for op in operations:
    if op == 1:
        array = flip(array, True)
    elif op == 2:
        array = flip(array, False)
    elif op == 3:
        array = rotate(array, True)
    elif op == 4:
        array = rotate(array, False)
    elif op == 5:
        array = move(array, True)
    elif op == 6:
        array = move(array, False)

for row in array:
    print(' '.join(map(str, row)))