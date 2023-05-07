from collections import Counter
from itertools import combinations

T = input()
N = int(input())
books = []
prices = []
for _ in range(N):
    p, b = input().split()
    prices.append(int(p))
    books.append(Counter(b))
finds = Counter(T)

results = []

tmp = [i for i in range(N)]

for i in range(1, N + 1):
    for comb in list(combinations(tmp, i)):
        union = Counter()
        for c in comb:
            union += books[c]
        if union & finds == finds:
            total = 0
            for index in comb:
                total += prices[index]
            results.append(total)

print(-1 if len(results) == 0 else min(results))