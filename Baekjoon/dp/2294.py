n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]
dp = [10001 for _ in range(k + 1)]
dp[0] = 0

for v in values:
    for i in range(v, k + 1):
        dp[i] = min(dp[i], dp[i - v] + 1)

print(dp[k] if dp[k] != 10001 else -1)