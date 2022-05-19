n, k = map(int, input().split())
stuff = []
dp = [0] * (k + 1)

for _ in range(n):
    w, v = map(int, input().split())
    stuff.append((w, v))
stuff.sort()

for s in stuff:
    for i in range(k, s[0] - 1, -1):
        dp[i] = max(dp[i], dp[i - s[0]] + s[1])

print(dp[-1])