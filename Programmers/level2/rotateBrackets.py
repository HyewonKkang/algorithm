def isValidParentheses(s):
    stack = []
    opened, closed = ['[', '(', '{'], [']', ')', '}']
    for p in s:
        if p in opened:
            stack.append(p)
        else:
            if not stack:
                return False
            for i in range(3):
                if p == closed[i] and stack[-1] == opened[i]:
                    stack.pop()
    return len(stack) == 0

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += isValidParentheses(s[i:] + s[0:i])
    return answer
