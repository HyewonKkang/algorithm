import math
def changeNotation(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return rev_base[::-1]


def isPrime(n, k):
    x = int(n)
    if x == 1: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    changed_base = changeNotation(n, k)
    nums = changed_base.split('0')
    for n in nums:
        if n != '' and isPrime(n, k):
            answer += 1
    return answer
