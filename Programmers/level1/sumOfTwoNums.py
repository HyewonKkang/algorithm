def solution(a, b):
    answer = 0

    if a == b:
        return a

    min_num = min(a, b)
    max_num = max(a, b)

    for i in range(min_num, max_num+1):
        answer += i

    return answer