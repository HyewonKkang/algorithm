def solution(s):
    result = list(s)
    result.sort(reverse=True)
    answer = ''.join(result)
    return answer

print(solution("Zbcdefg"))