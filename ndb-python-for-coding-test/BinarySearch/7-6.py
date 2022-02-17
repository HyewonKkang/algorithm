N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
start, end = 0, arr[N - 1]
res = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in range(N):
        if arr[i] > mid:
            total += arr[i] - mid
    if total < M:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)