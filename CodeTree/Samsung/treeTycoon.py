# 나무 타이쿤
n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
rules = [list(map(int, input().split())) for _ in range(m)]
directions = [(0, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
nutrients = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
tmp_pos = []
for i in range(n):
    row = []
    for j in range(n):
        row.append((i, j))
    tmp_pos.append(row * 5)
pos_arr = tmp_pos * 5

def moveNutrients(d, p):
    global nutrients
    direction = directions[d]
    for i, nutrient in enumerate(nutrients):
        prev_x, prev_y = nutrient
        next_x, next_y = pos_arr[n + prev_x + direction[0] * p][n + prev_y + direction[1] * p]
        nutrients[i] = (next_x, next_y)


def cutTree():
    result = []
    for i in range(n):
        for j in range(n):
            if area[i][j] >= 2 and (i, j) not in nutrients:
                area[i][j] -= 2
                result.append((i, j))
    return result


for rule in rules:
    # 영양제 이동, 투입
    d, p = rule # 이동 방향, 이동 칸 수
    moveNutrients(d, p)

    # 영양제 투입 위치 성장
    for nutrient in nutrients:
        x, y = nutrient
        area[x][y] += 1
    for nutrient in nutrients:
        x, y = nutrient
        for dx, dy in [(1, 1), (-1, -1), (-1, 1), (1, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if area[nx][ny] >= 1:
                area[x][y] += 1

    # 영양제 제외 영역 처리
    nutrients = cutTree()

print(sum([sum(row) for row in area]))