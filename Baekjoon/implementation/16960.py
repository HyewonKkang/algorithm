from itertools import combinations
n, m = map(int, input().split())
lamps = [list() for _ in range(n + 1)]

for i in range(n):
    tmp = list(map(int, input().split()))
    if tmp[0] != 0:
        lamps[i + 1] = tmp[1:]

switches = [i for i in range(1, m + 1)]
answer = 0
tmp_lamps = [i for i in range(1, n + 1)]

for combs in list(combinations(tmp_lamps, n - 1)):
    tmp = []
    for c in combs:
        tmp.append(lamps[c])
    sets = sorted(list(set(sum(tmp, []))))
    if [i for i in range(1, m + 1)] == sets:
        answer = 1
        break

print(answer)