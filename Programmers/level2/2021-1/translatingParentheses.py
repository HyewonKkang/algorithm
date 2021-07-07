def checkCorrect(s):
    left = 0
    right = 0
    for char in s:
        if char == '(':
            left += 1
        elif char == ')':
            right += 1
        if left < right:
            return False
    if left != right:
        return False
    else:
        return True

def transformation(p):
    if p == '':
        return p
    left = 0
    right = 0
    u = ''
    v = ''

    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        elif p[i] == ')':
            right += 1
        u += p[i]
        if left == right:
            v += p[i + 1:]
            break

    if checkCorrect(u):
        u += transformation(v)
        return u
    else:
        tmp = '('
        tmp += transformation(v)
        tmp += ')'
        u = u[1:-1]
        for char in u:
            if char == '(':
                tmp += ')'
            elif char == ')':
                tmp += '('
        return tmp


def solution(p):
    answer = transformation(p)
    return answer
