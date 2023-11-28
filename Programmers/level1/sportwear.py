def solution(n, lost, reserve):
    answer = 0
    wore = []
    counts = [1] * (n + 1)
    for i in range(1, n + 1):
        if i in lost:
            counts[i] -= 1
        if i in reserve:
            counts[i] += 1
    for i in range(1, n + 1):
        if counts[i] == 1:
            answer += 1
            counts[i] -= 1
        elif counts[i] == 2:
            answer += 1
            counts[i] -= 1
        elif counts[i] == 0:
            if i > 1 and counts[i - 1] >= 1:
                answer += 1
                counts[i - 1] -= 1
            elif i < n and counts[i + 1] >= 2:
                answer += 1
                counts[i + 1] -= 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))