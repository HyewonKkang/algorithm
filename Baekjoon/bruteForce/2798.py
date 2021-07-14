from itertools import combinations
N, M = map(int, input().split())
cards = list(map(int, input().split()))
totals = []

for card in list(combinations(cards, 3)):
    if sum(card) <= M:
        totals.append(sum(card))

totals.sort()
answer = totals[-1]

print(answer)