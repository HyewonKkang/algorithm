N = int(input())
count = 0
nums = [i for i in range(1, N + 1)]
start, end = 0, 0

total = 1
while start < N and end < N:
    if total < N:
        end += 1
    elif total == N:
        count += 1
        start += 1
        end = start + 1
    else:
        start += 1
    total = sum(nums[start:end+1])

print(count)