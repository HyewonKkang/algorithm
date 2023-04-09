def solution(x, y, n):
    INF = int(1e9)
    dp = [INF] * (y + 1)
    dp[x] = 0

    for i in range(x + 1, y + 1):
        if x <= i - n:
            dp[i] = min(dp[i], dp[i - n] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return -1 if dp[y] == INF else dp[y]
