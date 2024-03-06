n = int(input())
dp = [[0 for _ in range(10)] for _ in range(1002)]

for i in range(10):
    dp[1][i] = 1


for i in range(2, n + 2):
    for j in range(0, 10):
        dp[i][j] = sum(dp[i - 1][:j + 1])


print(dp[n + 1][9] % 10007)