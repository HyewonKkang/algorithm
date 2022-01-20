N, M = map(int, input().split())
bulbs = list(map(int, input().split()))
for i in range(M):
    command, a, b = map(int, input().split())
    if command == 1:
        bulbs[a - 1] = b
    elif command == 2:
        for k in range(a-1, b):
            bulbs[k] = (bulbs[k] + 1) % 2
    elif command == 3:
        bulbs[a-1:b] = [0] * (b - a + 1)
    elif command == 4:
        bulbs[a-1:b] = [1] * (b - a + 1)

for i in range(N):
    print(bulbs[i], end=' ')