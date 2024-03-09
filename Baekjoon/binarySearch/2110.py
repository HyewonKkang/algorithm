n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()
answer = 0

start, end = 1, houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    current = houses[0]
    count = 1

    for i in range(1, n):
        if houses[i] - current >= mid:
            count += 1
            current = houses[i]

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1


print(answer)