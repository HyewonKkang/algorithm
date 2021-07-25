N = int(input())
count = 0
for _ in range(N):
    letters = []
    flag = 0
    word = input()
    for i in range(len(word)):
        if i > 0 and word[i] == letters[-1]:
            continue
        if word[i] in letters:
            flag = 1
            break
        letters.append(word[i])
    if flag == 0:
        count += 1
print(count)
