s, p = input(), input()
answer = 0
tmp = ''
for alphabet in p:
    if tmp + alphabet in s:
        tmp += alphabet
    else:
        tmp = alphabet
        answer += 1


print(answer + 1)