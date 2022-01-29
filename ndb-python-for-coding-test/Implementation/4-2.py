N = int(input())

# 00분 00초 ~ 59분 59초
min = [i for i in range(60)]
sec = [i for i in range(60)]
cnt = 0
for i in range(60):
    for j in range(60):
        res = str(min[i]) + str(sec[j])
        if '3' in res:
            cnt += 1

res = 0
for num in range(N + 1):
    if '3' in str(num):
        res += 3600
    else:
        res += cnt
print(res)