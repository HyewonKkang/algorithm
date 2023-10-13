n = int(input())
solutions = sorted(list(map(int, input().split())))
i, j = 0, n - 1
answer = []
while i < j:
    answer.append(solutions[i] + solutions[j])

    if solutions[i] + solutions[j] == 0:
        answer = 0
        break
    if solutions[i] + solutions[j] < 0:
        i += 1
    else:
        j -= 1
print(0 if answer == 0 else min(answer, key=lambda x:abs(x)))
