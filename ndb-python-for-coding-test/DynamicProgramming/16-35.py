n = int(input())
dp = [0] * n
dp[0] = 1
i = j = k = 0
n2, n3, n5 = 2, 3, 5

for l in range(1, n):
    dp[l] = min(n2, n3, n5)
    if dp[l] == n2:
        i += 1
        n2 = dp[i] * 2
    if dp[l] == n3:
        j += 1
        n3 = dp[j] * 3
    if dp[l] == n5:
        k += 1
        n5 = dp[k] * 5
print(dp)
print(dp[n - 1])