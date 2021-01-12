N, K = map(int, input().split())
units = [int(input()) for _ in range(N)]
units.sort(reverse = True)
coins = 0
for unit in units:
    value = K // unit
    if value < 1:
        continue
    else:
        K -= value * unit
        coins += value
print(coins)