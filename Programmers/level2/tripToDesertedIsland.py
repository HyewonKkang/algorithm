from collections import deque


def solution(maps):
    answer = []
    maps = [list(s) for s in maps]

    def bfs(x, y):
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

        q = deque([(x, y)])
        value = 0

        while q:
            x_, y_ = q.popleft()
            if maps[x_][y_] == 'X': continue
            value += int(maps[x_][y_])
            maps[x_][y_] = 'X'

            for i in range(4):
                nx, ny = dx[i] + x_, dy[i] + y_

                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X':
                    q.append((nx, ny))
        return value

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X':
                total = bfs(i, j)
                answer.append(total)

    return sorted(answer) if len(answer) != 0 else [-1]
