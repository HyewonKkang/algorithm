n, k = map(int, input().split())
arr = list(map(int, input().split()))
counts = [0] * (max(arr) + 1)
i, j = 0, 0
res = 0

while j < n:
    if counts[arr[j]] >= k:
        counts[arr[i]] -= 1
        i += 1
    else:
        counts[arr[j]] += 1
        j += 1
    res = max(res, j - i)
print(res)