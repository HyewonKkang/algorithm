n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
dp = [[0, 0] for _ in range(301)]


for i in range(1, n + 1):
    if i == 1:
        dp[i] = [stairs[1], 1]
    elif i == 2:
        dp[i] = [stairs[1] + stairs[2], 2]
    if dp[i - 1][1] == 2:
        dp[i][0] = max(dp[i - 2][0] + stairs[i], dp[i - 3][0] + stairs[i - 1] + stairs[i])
        dp[i][1] = 2 if dp[i - 2][0] + stairs[i] < dp[i - 3][0] + stairs[i - 1] + stairs[i] else 1
    else:
        dp[i][0] = max(dp[i - 1][0] + stairs[i], dp[i - 2][0] + stairs[i])
        dp[i][1] = dp[i - 1][1] + 1 if dp[i - 1][0] > dp[i - 2][0] else 1

print(dp[n][0])

