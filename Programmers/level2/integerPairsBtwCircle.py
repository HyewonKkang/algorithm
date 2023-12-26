def solution(r1, r2):
    count = 0
    for x in range(1, r2):
        y2 = int((r2 ** 2 - x ** 2) ** 0.5)
        y1_ = r1 ** 2 - x ** 2 if x <= r1 else 0
        y1 = int(y1_ ** 0.5)
        count += y2 - y1
        count += 1 if y1 ** 2 == y1_ else 0
    count += 1

    return count * 4
