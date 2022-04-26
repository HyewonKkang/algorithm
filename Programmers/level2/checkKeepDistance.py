from collections import deque


def bfs(x, y, rooms):
    q = deque([[x, y]])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[False] * 5 for _ in range(5)]
    dist = 0
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if rooms[nx][ny] != 'X':
                    if rooms[nx][ny] == 'P':
                        return False
                    q.append([nx, ny])
        dist += 1
        if dist == 2:
            break
    return True


def solution(places):
    answer = []
    for place in places:
        flag = 1
        rooms = [list(room) for room in place]
        people = []
        for i in range(5):
            for j in range(5):
                if rooms[i][j] == 'P':
                    people.append((i, j))
        for person in people:
            if not bfs(person[0], person[1], rooms):
                flag = 0
                break
        answer.append(flag)
    return answer