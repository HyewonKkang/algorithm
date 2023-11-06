from itertools import combinations


def calc_score(a, b): # Apeach, Lion
    a_score, b_score = 0, 0
    for i in range(10):
        if a[i] == b[i] == 0: continue
        if a[i] >= b[i]:
            a_score += 10 - i
        else:
            b_score += 10 - i
    return a_score, b_score


def get_possible_combinations(arr, target):
    result = []

    for count in range(1, len(arr) + 1):
        for indexs in combinations(range(len(arr)), count):
            if sum([arr[i] for i in indexs]) == target:
                result.append(list(indexs))
    return result



def solution(n, info):
    answer = []
    max_diff = 0

    for i in range(n, -1, -1):
        scores = [info[i] + 1 for i in range(10)] + [i]
        possibles = get_possible_combinations(scores, n)

        for possible in possibles:
            lion_list = [scores[i] if i in possible else 0 for i in range(11)]
            apeach, lion = calc_score(info, lion_list)
            if apeach < lion:
                diff = lion - apeach
                if max_diff < diff:
                    max_diff = diff
                    answer = lion_list
                elif max_diff == diff:
                    for i in range(10, -1, -1):
                        if answer[i] > lion_list[i]:
                            break
                        elif answer[i] < lion_list[i]:
                            answer = lion_list
                            break
    return answer if max_diff != 0 else [-1]
