n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x:(x[1], x[0]))

cur = 0
answer = 0
for m in meetings:
    s, e = m
    if cur > s:
        continue
    else:
        cur = e
        answer += 1
print(answer)