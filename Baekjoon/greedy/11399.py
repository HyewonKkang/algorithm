N = int(input())
p_list = list(map(int, input().split()))
p_list.sort()

def sum_list(list, n):
    sum = 0
    for i in range(n):
        sum += list[i]
    return sum

answer = 0
for i in range(N):
    answer += sum_list(p_list, i+1)

print(answer)