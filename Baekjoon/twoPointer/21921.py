n, x = map(int, input().split())
visitors = list(map(int, input().split()))
greatest = sum(visitors[0:x])
value = greatest
counts = 1

for i in range(x, n):
    value -= visitors[i - x]
    value += visitors[i]
    if value == greatest:
        counts += 1
    elif value > greatest:
        greatest = value
        counts = 1

if greatest == 0:
    print("SAD")
else:
    print(greatest)
    print(counts)