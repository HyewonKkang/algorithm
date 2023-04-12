from collections import deque


def solution(n, m, section):
    answer = 0
    needed = deque(section)
    while needed:
        pos = needed.popleft()
        while needed and pos + m > needed[0]:
            needed.popleft()
        answer += 1

    return answer
