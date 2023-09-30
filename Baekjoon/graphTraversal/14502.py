from itertools import combinations
from collections import deque
import copy
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
maps_ = [list(map(int, input().split())) for _ in range(n)]
viruses, empty = [], []
for i in range(n):
    for j in range(m):
        if maps_[i][j] == 2: viruses.append((i, j))
        elif maps_[i][j] == 0: empty.append((i, j))

def count_zeros(matrix):
    zero_count = 0
    for row in matrix:
        zero_count += row.count(0)
    return zero_count

def spread(new_walls): # bfs
    q = deque(viruses)
    maps = copy.deepcopy(maps_)
    for w in new_walls:
        maps[w[0]][w[1]] = 1
    visited = [[False] * m for _ in range(n)]
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]: continue
            if maps[nx][ny] == 1 or (nx, ny) in new_walls: continue
            if (maps[nx][ny] == 2 and not visited[nx][ny]) or maps[nx][ny] == 0:
                q.append((nx, ny))
                maps[nx][ny] = 2
                visited[x][y] = True

    return count_zeros(maps)


answer = 0
for combs in list(combinations(empty, 3)):
    answer = max(answer, spread(combs))
print(answer)