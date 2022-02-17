N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())

if sum(arr) <= M:
    print(arr[N - 1])
else:
    res = 0
    start = 0
    end = arr[N - 1]
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in range(N):
            if arr[i] <= mid:
                total += arr[i]
            else:
                total += mid
        if total > M:
            end = mid - 1
        else:
            res = mid
            start = mid + 1
    print(res)