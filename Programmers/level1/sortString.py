def solution(strings, n):

    strings.sort()
    answer = []

    lists = []
    for word in strings:
        lists.append([word, word[n]])

    lists.sort(key=lambda x : x[1])

    for word in lists:
        answer.append(word[0])

    return answer