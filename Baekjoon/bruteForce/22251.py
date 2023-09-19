n, k, p, x = map(int, input().split())
#   0
# 1   2
#   3
# 4   5
#   6
lights = [[0, 1, 2, 4, 5, 6],
          [2, 5],
          [0, 2, 3, 4, 6],
          [0, 2, 3, 5, 6],
          [1, 2, 3, 5],
          [0, 1, 3, 5, 6],
          [0, 1, 3, 4, 5, 6],
          [0, 2, 5],
          [0, 1, 2, 3, 4, 5, 6],
          [0, 1, 2, 3, 5, 6]]
lights = list(map(set, lights))
current = str(x).zfill(k)
answer = 0
range_ = 9 if n >= 9 else n

for _num in range(1, n + 1):
    num = str(_num).zfill(k)
    count = 0
    for i, n in enumerate(num):
        a, b = set(lights[int(n)]), set(lights[int(current[i])])
        diff = (a - b) | (b - a)
        count += len(diff)
    if count > p: continue
    answer += 1

print(answer - 1)
