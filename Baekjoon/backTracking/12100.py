n = int(input())
answer = 0
directions = [0, 1, 2, 3] # 위, 오, 아래, 왼

def rotateClockwise(repeat, board):
    for _ in range(repeat):
        board = list(map(list, zip(*board[::-1])))
    return board

def slide(d, board):
    if d == 0:
        board = rotateClockwise(3, board)
        board = slideLeft(board)
        board = rotateClockwise(1, board)
    elif d == 1:
        board = rotateClockwise(2, board)
        board = slideLeft(board)
        board = rotateClockwise(2, board)
    elif d == 2:
        board = rotateClockwise(1, board)
        board = slideLeft(board)
        board = rotateClockwise(3, board)
    elif d == 3:
        board = slideLeft(board)
    return board

def slideLeft(board):
    tmp = []
    for row in board:
        changed = slideRowLeft(row)
        combined = combineRow(changed)
        result = slideRowLeft(combined)
        tmp.append(result)
    return [row[:] for row in tmp]

def slideRowLeft(row):
    tmp = [0] * n
    j = 0
    for i in range(n):
        if row[i] != 0:
            tmp[j] = row[i]
            j += 1
    return tmp

def combineRow(row):
    for i in range(n - 1):
        if row[i] == row[i + 1]:
            row[i] = row[i] * 2
            row[i + 1] = 0
    return row

def backtracking(count, board):
    global answer
    if count == 5:
        max_value = max([max(row) for row in board])
        answer = max(answer, max_value)
        return

    tmp = [row[:] for row in board]
    for d in directions:
        board = slide(d, board)
        backtracking(count + 1, board)
        board = tmp


arr = [list(map(int, input().split())) for _ in range(n)]
backtracking(0, arr)
print(answer)