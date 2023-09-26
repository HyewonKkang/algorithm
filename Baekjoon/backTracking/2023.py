import math
n = int(input())

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def backtracking(nums):
    if len(nums) == n:
        print(''.join(nums))
        return

    for i in range(1, 10):
        if isPrime(int(''.join(nums + [str(i)]))):
            nums.append(str(i))
            backtracking(nums)
            nums.pop()


backtracking([])