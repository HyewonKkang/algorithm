from bisect import bisect_left, bisect_right
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
dots = list(map(int, sys.stdin.readline().rstrip().split()))
dots.sort()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    left = bisect_left(dots, a)
    right = bisect_right(dots, b)
    print(right - left)
