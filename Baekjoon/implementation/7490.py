from itertools import product
t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    for ops in list(product(['+', '-', ' '], repeat=n - 1)):
        nums = [i for i in range(1, n + 1)]
        res = ''
        for i, num in enumerate(nums):
            res += str(num)
            res += ops[i] if i < n - 1 else ''
        calc = res.replace(' ', '')
        if eval(calc) == 0:
            lst.append(res)
    lst.sort()
    for l in lst:
        print(l)
    print()