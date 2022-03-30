n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for c in coins:
    # 만들 수 없는 금액을 찾으면 종료
    if target < c:
        break
    target += c
print(target)