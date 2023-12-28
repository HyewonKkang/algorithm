def getLargestDivision(num):
    if num == 1:
        return 0

    tmp = []
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if num // i <= 10000000:
                tmp.append(num // i)
            tmp.append(i)
    return max(tmp) if tmp else 1


def solution(begin, end):
    return [getLargestDivision(num) for num in range(begin, end + 1)]
