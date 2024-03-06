T = int(input())
dp = [0] * 100

for i in range(3):
    dp[i] = 1
dp[3] = 2
dp[4] = 2

for i in range(5, 100):
    dp[i] = dp[i - 1] + dp[i - 5]

for _ in range(T):
    N = int(input())
    print(dp[N - 1])