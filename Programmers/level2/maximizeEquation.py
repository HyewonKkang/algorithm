from itertools import permutations


def separate(exp):
    result = []
    n = ''
    for e in exp:
        if e.isdigit():
            n += e
        else:
            result.append(n)
            result.append(e)
            n = ''
    return result + [n]


def solution(expression):
    answer = []
    op_priorities = list(permutations(['+', '-', '*'], 3))
    separated = separate(expression)
    for priority in op_priorities:
        exp = separated[:]
        for op in priority:
            while op in exp:
                idx = exp.index(op)
                new_n = eval(''.join(exp[idx-1:idx+2]))
                exp = exp[:idx-1] + [str(new_n)] + exp[idx+2:]
        answer.append(abs(int(exp[0])))
    return max(answer)


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))