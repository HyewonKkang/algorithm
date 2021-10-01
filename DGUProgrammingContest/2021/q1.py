data = list(map(int, input().split()))
days = data[0]
flag = 0
for i in range(1, days + 1):
    flag = 0
    for j in range(i + 1, days + 1):
        if data[i] < data[j]:
            print(j, end= ' ')
            flag = 1
            break
    if flag == 0:
        print(-1, end = ' ')

