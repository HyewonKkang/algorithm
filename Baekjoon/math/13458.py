n = int(input())
candidates = list(map(int, input().split()))
main, sub = map(int, input().split())
answer = n

for c in candidates:
    c -= main
    if c > 0:
        answer += c // sub if c % sub == 0 else c // sub + 1


print(answer)