from itertools import product
T_list = []
for n in range(1, 45):
    T_list.append(n * (n + 1) / 2)

sum_list = list()
for i in list(product(T_list, repeat = 3)):
    sum_list.append(sum(i))

def Eureka(n):
    if n in sum_list:
        return 1
    else:
        return 0

T = int(input())
answer = list()
for _ in range(T):
    K = int(input())
    answer.append(Eureka(K))

for i in answer:
    print(i)