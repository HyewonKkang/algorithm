def getGCD(x, y):
    while y:
        x, y = y, x % y
    return x

def getLCM(x, y):
    return (x * y) // getGCD(x, y)

def solution(n, m):
    answer = [getGCD(n, m), getLCM(n, m)]
    return answer


print(solution(3, 12))
print(solution(2, 5))