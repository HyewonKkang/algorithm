from itertools import permutations
N, M = map(int, input().split())
new_list = [i for i in range(1, N+1)]
for i in permutations(new_list, M):
    for j in i:
        print(j, end=' ')
    print()