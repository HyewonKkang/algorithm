n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
cnt = 0
i = 0
j = n - 1
while i != j:
    total = arr[i] + arr[j]
    if total == x:
        cnt += 1
        i += 1
    else:
        if x < total:
            j -= 1
        else:
            i += 1
print(cnt)