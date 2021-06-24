from itertools import combinations

def solution(orders, course):
    answer = []
    dict = {}
    max_length = 0
    new_orders = []

    for order in orders:
        if len(order) > max_length:
            max_length = len(order)

    for order in orders:
        temp = list(order)
        temp.sort()
        new_orders.append(''.join(temp))

    for order in new_orders:
        tmp = list(order)
        for i in course:
            for combi in list(combinations(tmp, i)):
                input_ = ''.join(combi)
                if input_ in dict:
                    dict[input_] += 1
                else:
                    dict[input_] = 1

    length = [0 for i in range(max_length+1)]
    result = [[] for i in range(max_length+1)]

    for key in dict:
        for i in course:
            if len(key) == i and dict[key] > 1:
                if dict[key] > length[len(key)]:
                    length[len(key)] = dict[key]
                    result[i] = []
                    result[i].append(key)
                elif dict[key] == length[len(key)]:
                    result[i].append(key)
                break

    for list_ in result:
        for order in list_:
            if len(order) > 0:
                answer.append(order)

    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))