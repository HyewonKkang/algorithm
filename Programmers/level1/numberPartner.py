from collections import Counter


def solution(X, Y):
    x_count, y_count = Counter(X), Counter(Y)
    nums = sorted((x_count & y_count).elements(), reverse=True)
    new_num = ''.join(nums)
    num_length = len(new_num)
    if num_length == 0:
        return "-1"
    if new_num.count('0') == num_length:
        return "0"
    return new_num

