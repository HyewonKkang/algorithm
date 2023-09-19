n, m = map(int, input().split())
lectures = list(map(int, input().split()))
answer = int(1e9)
start, end = lectures[-1], sum(lectures)

while start <= end:
    mid = (start + end) // 2
    arr = []
    prev = 0
    for l in lectures:
        if prev + l <= mid:
            prev += l
        else:
            arr.append(prev)
            prev = l
    if prev > 0: arr.append(prev)
    if len(arr) <= m:
        end = mid - 1
        answer = max(arr)
    else:
        start = mid + 1

print(answer)
