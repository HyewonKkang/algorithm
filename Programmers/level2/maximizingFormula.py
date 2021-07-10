from itertools import permutations
def solution(expression):
    lists = []
    splits = []
    op = []
    num = ''
    for char in expression:
        if char == '+' or char == '-' or char == '*':
            op.append(char)
            splits.append(num)
            splits.append(char)
            num = ''
        else:
            num += char
    splits.append(num)

    used_op = list(set(op))
    temp = splits.copy()

    for priority in list(permutations(used_op, len(used_op))):
        priority = list(priority)
        for op_ in priority:
            while True:
                if op_ not in splits:
                    break
                for i in range(len(splits)):
                    if splits[i] == op_:
                        sub_str = splits[i-1] + splits[i] + splits[i+1]
                        splits[i-1] = str(eval(sub_str))
                        del(splits[i])
                        del(splits[i])
                        break
        lists.append(abs(int(splits[0])))
        splits = temp.copy()

    return max(lists)