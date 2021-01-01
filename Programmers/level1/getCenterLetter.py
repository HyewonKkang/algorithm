def solution(s):
    answer = ''

    n = len(s)
    if n % 2 != 0:
        return answer + s[n // 2]
    else:
        answer = s[n//2 - 1] + s[n//2]
        return answer

print(solution('abcde'))
print(solution('qwer'))