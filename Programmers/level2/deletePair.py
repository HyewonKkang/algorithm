from collections import deque
def solution(s):
    s = deque(s)
    if len(s) % 2 == 1 or len(s) == 1:
        return 0
    stack = list()
    for letter in s:
        if len(stack) == 0:
            stack.append(letter)
        elif stack[-1] != letter:
            stack.append(letter)
        else:
            stack.pop()
    if len(stack) != 0:
        return 0
    else:
        return 1

print(solution("baabaa"))
print(solution("cdcd"))