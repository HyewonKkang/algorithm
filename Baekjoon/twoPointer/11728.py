n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i, j = 0, 0
res = []

while True:
    if i == n or j == m:
        break
    if a[i] <= b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

if i == n:
    res.extend(b[j:])
elif j == m:
    res.extend(a[i:])

print(*res)