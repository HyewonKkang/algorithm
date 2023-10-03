from collections import deque

def solution(board):
    for i, row in enumerate(board):
        board[i] = list(row)

    robot, goal = (-1, -1), (-1, -1)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R': robot = (i, j)
            elif board[i][j] == 'G': goal = (i, j)

    q = deque([robot])
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    visited[robot[0]][robot[1]] = 1
    while q:
        x, y = q.popleft()
        if x == goal[0] and y == goal[1]: break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            while True:
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[i]):
                    nx -= dx
                    ny -= dy
                    break
                if board[nx][ny] == 'D':
                    nx -= dx
                    ny -= dy
                    break
                nx += dx
                ny += dy
            if visited[nx][ny]: continue
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    res = visited[goal[0]][goal[1]]
    return res - 1 if res else -1
