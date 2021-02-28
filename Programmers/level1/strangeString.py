def solution(s):
    answer = ''

    lists = s.split(' ')

    for word in lists:
        for i in range(len(word)):
            if i % 2 != 0:
                answer += word[i].lower()
            else:
                answer += word[i].upper()
        answer += ' '

    answer = answer[:-1]
    return answer

print(solution("try hello world"))