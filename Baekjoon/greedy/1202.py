import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
checked = [False] * k
jewels.sort()
bags.sort()
answer = 0
tmp = []

for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(tmp, -jewels[0][1])
        heapq.heappop(jewels)
    if tmp:
        answer -= heapq.heappop(tmp)

print(answer)