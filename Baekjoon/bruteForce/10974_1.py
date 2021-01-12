N = int(input())
from itertools import permutations
for i in list(permutations(range(1, N+1), N)):
    for j in i:
        print(j, end = ' ')
    print()