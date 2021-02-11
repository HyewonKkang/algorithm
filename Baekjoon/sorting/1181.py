N = int(input())
words = []

for _ in range(N):
    words.append(input())
words = list(set(words))
words = sorted(words)
words = sorted(words, key=len)
for x in words:
    print(x)