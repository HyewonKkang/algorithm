from itertools import combinations
nums = list(input() for _ in range(9))
dwarfs = list(map(int, nums))
dwarfs.sort()
for i in list(combinations(dwarfs, 7)):
    if sum(i) == 100:
        for j in i:
            print(j)
        break