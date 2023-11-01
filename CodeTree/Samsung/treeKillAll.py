# 나무박멸
import sys
sys.stdin = open("input3.txt", "r")

from collections import defaultdict
n, m, k, c = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
answer = 0
herbicides = defaultdict(int)


def grow():
    for x in range(n):
        for y in range(n):
            counts = 0
            if area[x][y] > 0:
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if area[nx][ny] > 0:
                        counts += 1
            area[x][y] += counts


def breed():
    result = [row[:] for row in area]
    for x in range(n):
        for y in range(n):
            neighbor = []
            if area[x][y] > 0:
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if (nx, ny) not in herbicides and area[nx][ny] == 0:
                        neighbor.append((nx, ny))
            if not neighbor: continue
            trees_count = area[x][y] // len(neighbor)
            for near in neighbor:
                nx, ny = near
                result[nx][ny] += trees_count
    return result


def select():
    tmp = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if area[x][y] <= 0: continue
            tmp[x][y] += area[x][y]
            for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
                for s in range(1, k + 1):
                    nx, ny = x + dx * s, y + dy * s
                    if nx < 0 or nx >= n or ny < 0 or ny >= n or area[nx][ny] <= 0:
                        break
                    tmp[x][y] += area[nx][ny]
    max_val = 0
    result = (-1, -1)
    for i in range(n):
        for j in range(n):
            if tmp[i][j] > max_val:
                max_val = tmp[i][j]
                result = (i, j)

    return result


def exterminate(x, y):
    global answer
    answer += area[x][y]
    area[x][y] = 0
    herbicides[(x, y)] = c + 1
    for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        for s in range(1, k + 1):
            nx, ny = x + dx * s, y + dy * s
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break
            if area[nx][ny] <= 0:
                herbicides[(nx, ny)] = c + 1
                break
            answer += area[nx][ny]
            area[nx][ny] = 0
            herbicides[(nx, ny)] = c + 1


for year in range(1, m + 1):
    # 나무 성장
    grow()

    # 나무 번식
    area = breed()


    # 제초제 뿌릴 칸 선택 후 박멸
    x, y = select()
    if x != -1 and y != -1:
        exterminate(x, y)

    # 제초제가 있는 칸 남은 년도 1씩 감소
    deleted = []
    for loc, val in herbicides.items():
        herbicides[loc] -= 1
        if herbicides[loc] == 0:
            deleted.append(loc)
    deleted.reverse()
    for d in deleted:
        herbicides.pop(d)

    # print(herbicides)
    # for row in area:
    #     print(*row)
    # print('----')


print(answer)