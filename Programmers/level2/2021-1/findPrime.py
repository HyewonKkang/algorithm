from itertools import permutations
def isPrime(n):
    if n == 1: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = []
    for i in range(1, len(numbers)+1):
        for n in list(map(''.join, permutations(numbers, i))):
            if n.startswith('0'): continue
            if n not in nums:
                if isPrime(int(n)):
                    answer += 1
                    nums.append(n)
    answer = len(nums)
    return answer


print(solution("17"))
print(solution("011"))