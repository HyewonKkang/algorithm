n, k = map(int, input().split())
stuff = [0]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
    w, v = map(int, input().split())
    stuff.append((w, v))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight, value = stuff[i]
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])