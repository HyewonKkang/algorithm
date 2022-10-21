from collections import Counter
def solution(want, number, discount):
    result = 0
    discountLen = len(discount)
    products = dict(zip(want, number))
    for i in range(0, discountLen - 10 + 1):
        if products == Counter(discount[i : i + 10]):
            result += 1
    return result

