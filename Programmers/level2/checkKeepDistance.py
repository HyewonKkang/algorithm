def checkRoom(room):
    for i in range(2, 7):
        for j in range(2, 7):
            if room[i][j] == 'P':
                # 한 칸 차이
                for diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if room[i + diff[0]][j + diff[1]] == 'P':
                        return 0
                # 대각선 차이
                for diff in [(1, 1), (-1, -1), (-1, 1), (1, -1)]:
                    ni, nj = i + diff[0], j + diff[1]
                    if room[ni][nj] == 'P' and (room[ni][j] == 'O' or room[i][nj] == 'O'):
                        return 0
                # 두 칸 차이
                for diff in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
                    ni, nj = i + diff[0], j + diff[1]
                    if room[ni][nj] == 'P' and room[i + diff[0] // 2][j + diff[1] // 2] != 'X':
                        return 0
    return 1


def solution(places):
    for i, place in enumerate(places):
        tmp = ['XXXXXXXXX'] * 2
        for row in place:
            tmp.append('XX' + row + 'XX')
        places[i] = tmp + ['XXXXXXXXX'] * 2
    return [checkRoom(room) for room in places]

# from collections import deque
#
#
# def bfs(x, y, rooms):
#     q = deque([[x, y]])
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     visited = [[False] * 5 for _ in range(5)]
#     dist = 0
#     while q:
#         x, y = q.popleft()
#         visited[x][y] = True
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
#                 if rooms[nx][ny] != 'X':
#                     if rooms[nx][ny] == 'P':
#                         return False
#                     q.append([nx, ny])
#         dist += 1
#         if dist == 2:
#             break
#     return True
#
#
# def solution(places):
#     answer = []
#     for place in places:
#         flag = 1
#         rooms = [list(room) for room in place]
#         people = []
#         for i in range(5):
#             for j in range(5):
#                 if rooms[i][j] == 'P':
#                     people.append((i, j))
#         for person in people:
#             if not bfs(person[0], person[1], rooms):
#                 flag = 0
#                 break
#         answer.append(flag)
#     return answer
