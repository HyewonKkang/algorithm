def solution(s):
    length = len(s)
    min_len = length
    for unit in range(1, length):
        converted = ''
        cnt = 1
        for i in range(0, len(s), unit):
            cmp = s[i:i + unit]
            if cmp == s[i+unit:i+unit*2]:
                cnt += 1
            else:
                if cnt != 1:
                    converted += str(cnt) + cmp
                else:
                    converted += cmp
                cnt = 1
        if len(converted) < min_len:
            min_len = len(converted)
    return min_len
