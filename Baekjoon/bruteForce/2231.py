N = int(input())
answer = 0
length = len(str(N))
for num in range(1, N+1):
    result = num
    for j in range(length, 0, -1):
        result += (num % 10**j) // 10**(j - 1)
    if result == N:
        answer = num
        break
print(answer)