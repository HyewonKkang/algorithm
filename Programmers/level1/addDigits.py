def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)

    return answer

print(solution(123))
print(solution(987))