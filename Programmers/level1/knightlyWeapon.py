def getNumberOfDivisors(n):
    count = 0
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            count += 1 if i == n // i else 2
    return count


def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        divisors = getNumberOfDivisors(i)
        answer += power if divisors > limit else divisors
    return answer
