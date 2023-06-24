h, w = map(int, input().split())
joi = [input() for _ in range(h)]
answer = [[-1] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if joi[i][j] == 'c':
            answer[i][j] = 0
        else:
            findIndex = str(joi[i][0:j]).rfind('c')
            if findIndex != -1:
                answer[i][j] = j - findIndex

for i in range(h):
    print(*answer[i])