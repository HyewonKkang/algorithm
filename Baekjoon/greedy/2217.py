N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort(reverse = True)
max = 0
for i in range(N):
    if rope[i] * (i+1) > max:
        max = rope[i] * (i+1)
print(max)