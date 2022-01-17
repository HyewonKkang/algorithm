N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
max1 = arr[0]
max2 = arr[1]
result = 0

result = (max1 * K + max2) * (M // (K + 1)) + max1 * (M % (K + 1))
print(result)