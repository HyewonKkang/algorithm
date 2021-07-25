L = int(input())
set = list(map(int, input().split()))
start = 0; end = 0
answer = 0
n = int(input())
if n < set[0]:
    set.append(0)
if n > set[len(set) - 1]:
    set.append(1001)
set.sort()
if n in set:
    pass
else:
    for i in range(len(set)):
        if set[i] > n:
            start = set[i-1] + 1
            end = set[i]-1
            answer = end - start + (end - n) * (n - start)
            break
print(answer)