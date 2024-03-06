n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]

dp = [0] * 301

for i in range(1, n + 1):
    if i == 1:
        dp[i] = [stairs[1], 1]
    elif i == 2:
        dp[i] = [stairs[1] + stairs[2], 2]
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])

