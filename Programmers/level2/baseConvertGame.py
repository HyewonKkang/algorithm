def convert(num, base):
    T = "0123456789ABCDEF"
    q, r = divmod(num, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n, t, m, p):
    answer = ''
    lists = []
    for i in range(t * m):
        value = convert(i, n)
        while len(value) != 0:
            lists.append(value[0])
            value = value[1:]

    for i in range(p-1, t * m, m):
        answer += lists[i]
    return answer


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))