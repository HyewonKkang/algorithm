def solution(brown, yellow):
    answer = []
    out = 0
    total = brown + yellow
    for i in range(1, total+1):
        if total % i != 0:
            continue
        for j in range(1, i+1):
            if i * j == total:
                if (4 + ((i - 2) + (j - 2)) * 2) == brown:
                    answer.append(i)
                    answer.append(j)
                    out = 1
        if out == 1:
            break


    return answer