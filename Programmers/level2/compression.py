def solution(msg):
    answer = []
    dict = []
    for i in range(1, 27):
        dict.append(chr(64+i))

    while len(msg) != 0:
        idx = 0
        for i in range(1, len(msg)+1):
            if msg[:i] in dict:
                w = msg[:i]
                idx = i
        answer.append(dict.index(msg[:idx])+1)
        msg = msg[idx:]
        if len(msg) != 0:
            c = msg[0]
            dict.append(w+c)

    return answer
