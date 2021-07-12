def solution(s):
    answer = []
    numOfTransform = 0
    numOfRemoved = 0

    while s != '1':
        s_ = ''
        for char in s:
            if char == '0':
                numOfRemoved += 1
            else:
                s_ += '1'
        c = len(s_)
        s = str(bin(c))[2:]
        numOfTransform += 1

    answer.append(numOfTransform)
    answer.append(numOfRemoved)
    return answer