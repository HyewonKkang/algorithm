K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))
start = 1
end = max(arr)
res = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(K):
        count += arr[i] // mid
    if count < N:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)