k = int(input())
d = [0] * 46 # B의 개수
d[1] = 1
for i in range(2, k + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[k - 1], d[k])