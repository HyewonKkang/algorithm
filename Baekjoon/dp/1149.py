n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
dp = [[int(1e9) for _ in range(3)] for _ in range(n)]

for i in range(3):
    dp[0][i] = costs[0][i]

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if k == j: continue
            dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i][j])
print(min(dp[n - 1]))
