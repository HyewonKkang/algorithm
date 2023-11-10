import sys
input = sys.stdin.readline

n = int(input())
preferences = {}
classroom = [[0] * n for _ in range(n)]
empty_cells = [[0] * n for _ in range(n)]
done = []

for _ in range(n ** 2):
    input_ = list(map(int, input().split()))
    preferences[input_[0]] = input_[1:]

for i in range(n):
    for j in range(n):
        if i != 0 and j != 0 and i != n - 1 and j != n - 1:
            empty_cells[i][j] = 4
            continue
        if (i == 0 and j == 0) or (i == 0 and j == n - 1) or (i == n - 1 and j == 0) or (i == n - 1 and j == n - 1):
            empty_cells[i][j] = 2
        else:
            empty_cells[i][j] = 3

def re_calc_empty_cells(index):
    x, y = index
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
        if empty_cells[nx][ny] > 0:
            empty_cells[nx][ny] -= 1

def find_max_near_likes(cur):
    max_likes_count = 0
    index = []
    for x in range(n):
        for y in range(n):
            if not classroom[x][y]:
                likes = 0
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
                    if classroom[nx][ny] in preferences[cur]:
                        likes += 1
                if max_likes_count < likes:
                    max_likes_count = likes
                    index = [(x, y)]
                elif max_likes_count == likes:
                    index.append((x, y))
    return index

def find_max_near_empty(near):
    max_value = 0
    max_index = None
    for pos in near:
        x, y = pos
        if empty_cells[x][y] > max_value:
            max_index = (x, y)
            max_value = empty_cells[x][y]
    return max_index if max_index else near[0]

def find_available_cell(cur):
    near_likes = find_max_near_likes(cur)
    if len(near_likes) == 1:
        return near_likes[0]
    elif len(near_likes) > 1:
        near_empty = find_max_near_empty(near_likes)
        if near_empty:
            return near_empty


def add_near_satisfaction(x, y):
    res = 0
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
        if classroom[nx][ny] in preferences[classroom[x][y]]:
            res += 1
    return 10 ** (res - 1) if res else 0

def calc_total_satisfaction():
    answer = 0
    for i in range(n):
        for j in range(n):
            answer += add_near_satisfaction(i, j)
    return answer

for student in preferences.keys():
    near_student = 0
    for done_student in done:
        if student in preferences[done_student]:
            near_student = done_student
            break
    else:
        x, y = find_available_cell(student)
        classroom[x][y] = student
        re_calc_empty_cells((x, y))



print(calc_total_satisfaction())
