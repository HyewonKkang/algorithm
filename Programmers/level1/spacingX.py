def solution(x, n):
    answer = []
    cnt = x
    while len(answer) != n:
        answer.append(x)
        x += cnt

    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))