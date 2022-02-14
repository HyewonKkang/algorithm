import sys
from itertools import permutations
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
cards = [sys.stdin.readline().rstrip() for _ in range(n)]
arr = []

for per in list(permutations(cards, k)):
    tmp = ''
    for num in per:
        tmp += num
    arr.append(int(tmp))

print(len(list(set(arr))))
