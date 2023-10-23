n = int(input())
assignments = [list(map(int, input().split())) for _ in range(n)]
assignments.sort(key=lambda x:-x[1])
tmp = [0] * 1001

for a in assignments:
    daysLeft, score = a
    while tmp[daysLeft] != 0:
        daysLeft -= 1
    if daysLeft > 0:
        tmp[daysLeft] = score

print(sum(tmp))
