board = [list(map(int, input().split())) for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]
numbers = sum(numbers, [])
checked = [[False] * 5 for _ in range(5)]

def findNum(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                return (i, j)
    return (-1, -1)

def checkBingo():
    count = 0
    # 가로
    for i in range(5):
        if all(checked[i]): count += 1

    # 세로
    for j in range(5):
        for i in range(5):
            if not checked[i][j]: break
        else:
            count += 1

    # 대각선
    for i in range(5):
        if not checked[i][i]: break
    else:
        count += 1

    for i in range(5):
        if not checked[i][4 - i]: break
    else:
        count += 1

    return True if count >= 3 else False


for i, num in enumerate(numbers):
    x, y = findNum(num)
    checked[x][y] = True

    if checkBingo():
        print(i + 1)
        break
