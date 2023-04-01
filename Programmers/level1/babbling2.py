import re


def solution(babbling):
    answer = 0

    for word in babbling:
        babblings = re.findall('aya|ye|woo|ma', word)
        if ''.join(babblings) != word:
            continue
        flag = 1
        for i in range(1, len(babblings)):
            if babblings[i - 1] == babblings[i]:
                flag = 0
                break
        answer += flag

    return answer
