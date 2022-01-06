A, B = map(int, input().split())
result = 1

while A < B:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        result = -1
        break
    result += 1
if A == B:
    print(result)
else:
    print(-1)
