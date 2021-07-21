n = int(input())
answer = 0
while n > 0:
    if n % 5 == 0:
        print(n // 5 + answer)
        break

    n -= 2
    answer += 1

if n < 0:
    print(-1)