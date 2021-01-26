from collections import deque
def solution(s):
    answer = True
    queue = deque()
    for letter in s:
        if letter == '(':
            queue.append(letter)
        else:
            if len(queue) == 0:
                return False
            queue.popleft()

    if len(queue) != 0:
        return False
    return answer

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))