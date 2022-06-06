def isPalindrome(word):
    if word == word[::-1]:
        return len(word)
    else:
        return -1


def solution(s):
    answer = 1
    length = len(s)

    for i in range(length):
        for j in range(i + 1, length):
            tmp = isPalindrome(s[i : j + 1])
            if tmp > -1:
                answer = max(answer, tmp)
    return answer
