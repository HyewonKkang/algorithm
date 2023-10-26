k, n = map(int, input().split())
cables = sorted([int(input()) for _ in range(k)])
start, end = 1, cables[-1]
answer = 0

def binary_search(start, end):
    global answer
    while start <= end:
        mid = (start + end) // 2
        counts = sum([c // mid for c in cables])
        if counts < n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

binary_search(start, end)
print(answer)