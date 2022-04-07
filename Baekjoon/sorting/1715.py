import heapq
n = int(input())
cards = list(int(input()) for _ in range(n))
heapq.heapify(cards)

res = 0
while len(cards) != 1:
    n1 = heapq.heappop(cards)
    n2 = heapq.heappop(cards)
    total = n1 + n2
    res += total
    heapq.heappush(cards, total)

print(res)