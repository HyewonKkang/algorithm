def solution(money):
    answer = 0
    l = len(money)
    dp1 = [0] * l
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    dp1[2] = max(dp1[0] + money[2], dp1[1])
    for i in range(3, len(money) - 1):
        dp1[i] = max(dp1[i - 3] + money[i], dp1[i - 2] + money[i], dp1[i - 1])

    dp2 = [0] * l
    dp2[0] = 0
    dp2[1] = money[1]
    dp2[2] = max(money[1], money[2])
    for i in range(3, len(money)):
        dp2[i] = max(dp2[i - 3] + money[i], dp2[i - 2] + money[i], dp2[i - 1])

    return max(dp1 + dp2)