def solution(s):
    answer = ''
    s = s.lower()
    word_list = s.split(' ')
    for word in word_list:
        word = word.capitalize()
        answer += word + ' '
    answer = answer[:-1]
    return answer

print(solution("3people     Unfollowed Me"))
print(solution("for the last week"))