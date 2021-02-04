def solution(new_id):
    answer = ''
    new_id = new_id.lower() # step 1

    symbols = ['-', '_', '.']
    for letter in new_id: # step 2
        if letter.isalpha():
            answer += letter
        if letter.isdigit():
            answer += letter
        if letter in symbols:
            answer += letter

    stack = [] # step 3
    for letter in answer:
        if len(stack) == 0:
            stack.append(letter)
        elif letter != '.':
            stack.append(letter)
        else:
            if stack[-1] != '.':
                stack.append(letter)

    answer = ''.join(stack)

    if len(answer) == 1:
        if answer.startswith('.'): # step 4
            answer = answer[1:]
    elif len(answer) > 1:
        if answer.startswith('.'):
            answer = answer[1:]
        if answer.endswith('.'):
            answer = answer[:len(answer)-1]

    if len(answer) == 0: # step 5
        answer = 'a'

    if len(answer) >= 16: # step 6
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 3: # step 7
        while len(answer) != 3:
            answer += answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
