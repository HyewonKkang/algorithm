N, M = map(int, input().split())
d = [-1] * 10001
values = []

for i in range(N):
    num = int(input())
    d[num] = 1
    values.append(num)

for i in range(values[0], M + 1):
    if d[i] != -1:
        continue
    tmp = []
    for j in values:
        if d[i - j] != -1:
            tmp.append(d[i - j] + 1)
    if tmp:
        d[i] = min(tmp)
print(d[M])
