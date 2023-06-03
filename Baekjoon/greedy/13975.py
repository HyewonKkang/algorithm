import sys
import heapq


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    counts = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    cost = 0
    while len(files) > 1:
        added = heapq.heappop(files) + heapq.heappop(files)
        cost += added
        files.append(added)
    print(cost)
