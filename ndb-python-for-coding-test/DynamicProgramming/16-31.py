t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    arr = []
    i = 0
    for _ in range(n):
        arr.append(tmp[i:i+m])
        i += m
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = arr[i][0]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1]) + arr[i][j]
            elif i == n - 1:
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1]) + arr[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + arr[i][j]
    tmp = list(dp[i][m - 1] for i in range(n))
    print(max(tmp))
