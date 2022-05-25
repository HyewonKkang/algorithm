n, k = map(int, input().split())
rocks = [0] + list(map(int, input().split()))
max_int = int(1e9)
dp = [max_int] * (n + 1)
dp[1] = rocks[1]
for i in range(1, n + 1):
    for j in range(1, i):
        tmp = (i - j) * (1 + abs(rocks[i] - rocks[j]))
        if tmp <= k:
            dp[i] = min(dp[i], dp[j] + tmp)

if dp[n] != max_int:
    print("YES")
else:
    print("NO")