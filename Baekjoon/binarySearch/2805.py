N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)
res = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in range(N):
        if trees[i] > mid:
            total += trees[i] - mid
    if total < M:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)