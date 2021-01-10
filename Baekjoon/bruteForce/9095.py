T = int(input())
def addWith123(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return addWith123(n-1) + addWith123(n-2) + addWith123(n-3)

for i in range(T):
    num = int(input())
    print(addWith123(num))

