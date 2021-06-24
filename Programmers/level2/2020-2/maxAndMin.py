def solution(s):
    answer = ''
    num = s.split(' ')
    num = list(map(int, num))
    max_num = max(num)
    min_num = min(num)
    answer += str(min_num) + ' ' + str(max_num)
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))