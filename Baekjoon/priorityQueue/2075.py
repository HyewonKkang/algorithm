import sys
import heapq
N = int(input())
heap = []
heapq.heapify(heap)
for i in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    if i == 0:
        for n in nums:
            heapq.heappush(heap, n)
        min_num = heap[0]
    else:
        for n in nums:
            if n > min_num:
                heapq.heappush(heap, n)
                heapq.heappop(heap)
                min_num = heap[0]
print(heap[0])

