def combinations(N, M):
    result = 1
    if N != M:
        for i in range(M, M - N, -1):
            result *= i
        for i in range(N, 0, -1):
            result //= i
    return result


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(combinations(N, M))
