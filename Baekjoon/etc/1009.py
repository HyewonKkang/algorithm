T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    remainder = [a%10]
    for i in range(10):
        r = (remainder[-1] * a) % 10
        if r in remainder:
            break
        else:
            remainder.append(r)
    result = remainder[b % len(remainder)-1]
    if result == 0:
        print(10)
    else:
        print(result)