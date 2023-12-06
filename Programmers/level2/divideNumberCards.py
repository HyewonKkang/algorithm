from math import gcd

def lst_gcd(lst):
    res = lst[0]
    for n in lst:
        res = gcd(res, n)
    return res

def solution(arrayA, arrayB):
    answer = 0
    gcdA, gcdB = lst_gcd(arrayA), lst_gcd(arrayB)
    if gcdA > 1:
        for n in arrayB:
            if n % gcdA == 0: break
        else:
            answer = max(answer, gcdA)
    if gcdB > 1:
        for n in arrayA:
            if n % gcdB == 0: break
        else:
            answer = max(answer, gcdB)

    return answer
