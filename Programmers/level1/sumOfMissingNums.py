def solution(numbers):
    total = sum([i for i in range(0, 10)])
    for n in numbers:
        total -= n
    return total
