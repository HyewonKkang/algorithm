N = int(input())
res = 0
cows = {}

for i in range(N):
    num, loc = map(int, input().split())
    if num in cows and cows[num] != loc:
        res += 1
    cows[num] = loc
print(res)
