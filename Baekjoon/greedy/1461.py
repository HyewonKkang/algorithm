n, m = map(int, input().split())
books = sorted(list(map(int, input().split())))
criteria = n
answer = 0
for i, b in enumerate(books):
    if b > 0:
        criteria = i
        break
negative, positive = books[:criteria], books[criteria:]
for i in range(0, len(negative), m):
    answer += -negative[i] * 2
for i in range(len(positive) - 1, -1, -m):
    answer += positive[i] * 2
absNums = [abs(b) for b in books]
print(answer - max(absNums))
