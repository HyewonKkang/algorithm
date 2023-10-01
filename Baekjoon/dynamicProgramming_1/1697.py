n, k = map(int, input().split())
dp = [int(1e9)] * (k * 2 + 1)

if n >= k:
    print(n - k)
else:
    dp[n] = 0
    for i in range(0, n):
        dp[i] = n - i
    for i in range(1, k * 2 + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
        if i % 2 == 0 and 0 <= i // 2 <= k:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        if 0 <= i - 1 <= k:
            dp[i - 1] = min(dp[i - 1], dp[i] + 1)

    print(dp[k])