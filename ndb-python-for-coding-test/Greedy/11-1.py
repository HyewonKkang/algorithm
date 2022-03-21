n = int(input())
fear = list(map(int, input().split()))
fear.sort()
total = 0
cnt = 0
for f in fear:
    cnt += 1
    if cnt >= f:
        total += 1
        cnt = 0
print(total)