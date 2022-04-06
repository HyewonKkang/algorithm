from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
arr = list(map(int, input().split()))

def count_by_range():
    right = bisect_right(arr, x)
    left = bisect_left(arr, x)
    return right - left

count = count_by_range()
if count == 0:
    print(-1)
else:
    print(count)