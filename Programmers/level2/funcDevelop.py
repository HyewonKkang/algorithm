import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = deque()
    stack = []

    for i in range(len(progresses)):
        queue.append(math.ceil((100 - progresses[i]) / speeds[i]))

    cnt = 1
    while len(queue) != 0:
        if not stack:
            stack.append(queue.popleft())
            continue
        if stack[-1] < queue[0]:
            answer.append(cnt)
            stack.clear()
            cnt = 1
        else:
            cnt += 1
            queue.popleft()
    answer.append(cnt)

    return answer
