def getReverseTernary(n):
    res = ''
    while n > 0:
        n, mod = divmod(n, 3)
        res += str(mod)
    return res

def solution(n):
    ternary = getReverseTernary(n)
    return int(ternary, 3)
