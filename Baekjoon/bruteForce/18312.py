def addZero(str):
    if len(str) == 1:
        return '0' + str
    return str

N, K = map(int, input().split())
answer = 0

for i in range(0, N+1):
    for j in range(0, 60):
        for k in range(0, 60):
            new_time = addZero(str(i)) + ':' + addZero(str(j)) + ':' + addZero(str(k))
            if str(K) in new_time:
                answer += 1
print(answer)