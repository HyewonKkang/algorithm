a, p = map(int, input().split())
d = [a]

while True:
    res = 0
    for n in list(str(d[-1])):
        res += int(n) ** p
    if res in d:
        break
    d.append(res)
print(d.index(res))