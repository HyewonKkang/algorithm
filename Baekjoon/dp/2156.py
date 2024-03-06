n = int(input())
wine = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)
dp[1] = wine[1]

if n >= 2:
    dp[2] = wine[1] + wine[2]
elif n >= 3:
    dp[3] = max(wine[1] + wine[3], wine[2] + wine[3], dp[2])

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + wine[i], wine[i - 1] + wine[i] + dp[i - 3], dp[i - 1])

print(dp[n])