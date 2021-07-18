def correctBrackets(str):
    stack = []
    for s in str:
        if s == '(' or s == '[' or s == '{':
            stack.append(s)
        else:
            if not stack:
                return False
            if s == ')' and stack[-1] == '(':
                stack.pop()
            elif s == ']' and stack[-1] == '[':
                stack.pop()
            elif s == '}' and stack[-1] == '{':
                stack.pop()

    if len(stack) != 0:
        return False

    return True

def solution(s):
    answer = 0
    for i in range(len(s)):
        str1 = s[0]
        str2 = s[1:]
        s = str2 + str1
        if correctBrackets(s):
            answer += 1

    return answer