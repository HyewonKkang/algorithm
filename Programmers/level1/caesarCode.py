def solution(s, n):
    answer = ''

    for letter in s:
        if letter == ' ':
            answer += letter
        else:
            if letter.isupper():
                answer += chr(65 + (ord(letter) + n - 65) % 26)
            elif letter.islower():
                answer += chr(97 + (ord(letter) + n - 97) % 26)
    return answer
