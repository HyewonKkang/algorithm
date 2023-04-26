def checkIsGameDone(board, found):
    winSet = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]

    for condition in winSet:
        a, b, c = condition
        if board[a] == board[b] == board[c] and board[a] == found:
            return True
    return False


def solution(board):
    board_ = sum([list(board[i]) for i in range(3)], [])
    first, second = board_.count('O'), board_.count('X')
    if first < second or first - second > 1:
        return 0
    elif first == second and checkIsGameDone(board_, 'O'):
        return 0
    elif first > second and checkIsGameDone(board_, 'X'):
        return 0
    return 1
