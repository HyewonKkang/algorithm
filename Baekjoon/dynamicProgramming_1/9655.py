N = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 2
for i in range(3, N + 1):
    d[i] = min(d[i - 3] + 1, d[i - 1] + 1)
if d[N] % 2 == 0:
    print("CY")
else:
    print("SK")
