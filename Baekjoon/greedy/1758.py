N = int(input())
tips = [int(input()) for i in range(N)]
answer = 0

tips.sort(reverse=True)

for i in range(len(tips)):
    tip = tips[i] - i
    if tip > 0:
        answer += tip
print(answer)