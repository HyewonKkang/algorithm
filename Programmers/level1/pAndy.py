def solution(s):
    p_cnt = 0
    y_cnt = 0
    s = s.lower()
    for letter in s:
        if letter == 'p':
            p_cnt += 1
        elif letter == 'y':
            y_cnt += 1

    if p_cnt == y_cnt:
        return True
    else:
        return False

