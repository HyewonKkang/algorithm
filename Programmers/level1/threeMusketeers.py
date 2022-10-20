from itertools import combinations
def solution(number):
    result = 0
    for sets in list(combinations(number, 3)):
        if sum(sets) == 0:
            result += 1
    return result

