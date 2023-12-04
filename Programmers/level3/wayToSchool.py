def solution(m, n, puddles):
    dp = [[1] * m for _ in range(n)]
    for pud in puddles:
        y, x = pud
        dp[x - 1][y - 1] = 0
        if x - 1 == 0:
            while y - 1 < m:
                dp[x - 1][y - 1] = 0
                y += 1
        if y - 1 == 0:
            while x -1 < n:
                dp[x - 1][y - 1] = 0
                x += 1

    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == 0: continue
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n - 1][m - 1]
