# 놀이기구 탑승
n = int(input())
board = [[0] * n for _ in range(n)]
preferences = {}
students = []
for _ in range(n ** 2):
    lst = list(map(int, input().split()))
    students.append(lst[0])
    preferences[lst[0]] = lst[1:]
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
answer = 0

def getPos(student):
    available = []
    for x in range(n):
        for y in range(n):
            near, empty = 0, 0
            if board[x][y]: continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if board[nx][ny] == 0:
                    empty += 1
                elif board[nx][ny] in preferences[student]:
                    near += 1
            available.append((-near, -empty, x, y))
    available.sort()
    return (available[0][2], available[0][3])


for student in students:
    x, y = getPos(student)
    board[x][y] = student

for x in range(n):
    for y in range(n):
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if board[nx][ny] in preferences[board[x][y]]:
                count += 1
        answer += 10 ** (count - 1) if count > 0 else 0

print(answer)