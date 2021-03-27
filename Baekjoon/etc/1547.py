answer = -1
M = int(input())
cups = [0, 1, 2, 3]
for i in range(M):
    a, b = map(int, input().split())
    tmp = cups[a]
    cups[a] = cups[b]
    cups[b] = tmp
for i in range(len(cups)):
    if cups[i] == 1:
        print(i)
        break
print(answer)