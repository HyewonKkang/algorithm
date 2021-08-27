import math
def solution(n):
    answer = math.sqrt(n)
    if int(answer) == answer:
        answer += 1
        return int(answer ** 2)
    else:
        return -1

print(solution(121))
print(solution(3))