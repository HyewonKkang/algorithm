N, M = map(int, input().split())
arr = []
result = 0
for i in range(N):
    line = list(map(int, input().split()))
    minimum = min(line)
    if result < minimum:
        result = minimum
print(result)