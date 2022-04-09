from itertools import combinations
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if map[i][j] == 2:
            chickens.append((i, j))
        elif map[i][j] == 1:
            houses.append((i, j))

res = []
for comb_chickens in list(combinations(chickens, m)):
    total = 0
    for house in houses:
        min_val = 100
        for chicken in comb_chickens:
            dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            min_val = min(dist, min_val)
        total += min_val
    res.append(total)
print(min(res))