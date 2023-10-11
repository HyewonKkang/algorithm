from bisect import bisect_left, bisect_right
n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
finds = list(map(int, input().split()))
answer = []

for num in finds:
    l, r = bisect_left(cards, num), bisect_right(cards, num)
    answer.append(r - l)

print(*answer)

