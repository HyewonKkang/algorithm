def solution(a, b):
    answer = ''
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    n = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    value = 0
    for i in range(a-1):
        value += n[i]
    value += b

    answer = days[value % 7 - 1]

    return answer

print(solution(1, 1))
print(solution(5, 24))