A = int(input())
T = int(input())
sign = input()

game = ''
cnt = 1
while len(game) <= A * T:
    game += '0101'
    for i in range(cnt + 1):
        game += '0'
    for i in range(cnt + 1):
        game += '1'
    cnt += 1

cnt = 0
answer = 0
for i in range(len(game)):
    if game[i] == sign:
        cnt += 1
        if cnt == T:
            answer = i % A
            break

print(answer)
