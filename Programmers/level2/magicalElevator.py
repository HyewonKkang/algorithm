def solution(storey):
    answer = 0

    while storey > 0:
        remainder = storey % 10
        if remainder < 5:
            storey -= remainder
        elif remainder == 5:
            if (storey // 10) % 10 >= 5:
                storey += (10 - remainder)
                remainder = 10 - remainder
            else:
                storey -= remainder
        else:
            storey += (10 - remainder)
            remainder = 10 - remainder

        answer += remainder
        storey //= 10

    return answer
