import sys
import heapq

input = sys.stdin.readline
n = int(input())
q = []

for _ in range(n):
    s, t = map(int, input().split())
    flag = 0
    q.append((s, t))

q.sort()

rooms = []
heapq.heappush(rooms, q[0][1])

for i in range(1, n):
    if q[i][0] >= rooms[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, (q[i][1]))

print(len(rooms))