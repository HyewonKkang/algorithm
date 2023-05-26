from itertools import chain
import sys
sys.setrecursionlimit(10**6)

n = int(input())
areas = [list(map(int, input().split())) for _ in range(n)]
heights = set(chain(*areas))
answer = 0


def dfs(x, y, height, visited):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if not visited[x][y] and areas[x][y] > height:
        visited[x][y] = True
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            dfs(nx, ny, height, visited)
        return True
    return False


for rainHeight in heights:
    visited = [[False] * n for _ in range(n)]
    safeArea = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j, rainHeight, visited):
                safeArea += 1
    answer = max(answer, safeArea)
print(answer if answer > 0 else 1)
