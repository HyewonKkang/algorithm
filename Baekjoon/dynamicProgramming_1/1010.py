T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(m + 1):
        d[1][i] = i
    for i in range(2, n + 1):
        for j in range(i, m + 1):
            if i == j:
                d[i][j] = 1
                continue
            if d[i][j] == 0:
                d[i][j] = d[i - 1][j - 1] + d[i][j - 1]
    print(d[n][m])
