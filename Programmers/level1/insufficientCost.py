def solution(price, money, count):
    total = 0
    for c in range(1, count + 1):
        total += c * price
    if total > money:
        return (total - money)
    else:
        return 0