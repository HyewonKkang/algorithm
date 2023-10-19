from collections import deque
n = int(input())
arr = []
shark_pos = (-1, -1)
shark = 2
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 9:
            shark_pos = (i, j)
    arr.append(row)
answer = 0

def getDistance():
    q = deque([(shark_pos[0], shark_pos[1])])
    visited = [[0] * n for _ in range(n)]
    visited[shark_pos[0]][shark_pos[1]] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and arr[nx][ny] <= shark:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return visited


def nextFish():
    result = []
    fishes = [fish for row in arr for fish in row]
    distance_table = getDistance()
    for i in range(n ** 2):
        if 1 <= fishes[i] < shark:
            distance = distance_table[i // n][i % n]
            if distance > 0:
                result.append((distance, i // n, i % n))
    result.sort()
    return result[0] if result else []

ate = 0
while True:
    next = nextFish()
    if not next:
        break
    time, x, y = next
    arr[x][y] = 0
    arr[shark_pos[0]][shark_pos[1]] = 0
    ate += 1
    if ate == shark:
        shark += 1
        ate = 0
    shark_pos = (x, y)
    answer += time

print(answer)