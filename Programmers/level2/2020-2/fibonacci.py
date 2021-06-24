# solved with recursion, time-over
# def solution(n):
#     if n == 0 or n == 1:
#         return n
#     return solution(n-1) + solution(n-2)
#
# print(solution(3))
# print(solution(5))

def solution(n):
    answer = 0
    f1 = 1; f0 = 0
    if n == 0 or n == 1:
        return n
    else:
        for i in range(1, n):
            answer = f1 + f0
            f0 = f1
            f1 = answer
        return answer%1234567

print(solution(3))
print(solution(5))