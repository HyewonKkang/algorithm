from itertools import product
N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
for i in product(nums, repeat = M):
    for j in i:
        print(j, end = ' ')
    print()