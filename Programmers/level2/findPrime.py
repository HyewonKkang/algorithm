from itertools import permutations
def isPrime(n):
    n = int(n)
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = list(numbers)
    num_list = []
    for i in range(1, len(numbers)+1):
        for j in list(permutations(nums, i)):
            new_num = ''
            for k in j:
                new_num += k
            if new_num not in num_list:
                if new_num.startswith('0'):
                    continue
                else:
                    if isPrime(new_num):
                        answer += 1
                    num_list.append(new_num)
    return answer