from collections import deque
def solution(sentence, keyword, skips):
    encrypted = ''
    skips = deque(skips)
    idx = 0
    key_idx = 0
    key_len = len(keyword)
    length = len(sentence)

    while skips:
        skip = skips.popleft()
        cur = keyword[key_idx % key_len]
        dup = sentence[idx:idx+skip].find(cur)
        if dup < 0:
            encrypted += sentence[idx:idx+skip]
            idx += skip
            if idx > length: break
            encrypted += cur
        else:
            encrypted += sentence[idx:idx+dup + 1]
            idx += dup + 1
            if idx > length: break
            encrypted += cur
        key_idx += 1

    encrypted += sentence[idx:]
    return encrypted



print(solution("i love coding", "mask", [0,0,3,2,3,4]))
print(solution("i love coding", "mode", [0, 10]))
print(solution("abcde fghi", "axyz", [3, 9, 0, 1]))
print(solution("encrypt this sentence", "something", [0, 1, 3, 2, 9, 2, 0, 3, 0, 2, 4, 1, 3]))