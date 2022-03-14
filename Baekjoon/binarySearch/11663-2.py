import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
dots = list(map(int, sys.stdin.readline().rstrip().split()))
dots.sort()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if dots[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    left = start
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if dots[mid] > b:
            end = mid - 1
        else:
            start = mid + 1
    right = end
    print(right - left + 1)