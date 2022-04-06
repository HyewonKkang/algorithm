def solution(N, stages):
    answer = []
    count = [0] * (N + 2)

    for s in stages:
        count[s] += 1

    for i in range(1, N + 1):
        total = sum(count[i:])
        if total != 0:
            answer.append((i, count[i] / total))
        else:
            answer.append((i, 0))

    answer.sort(key=lambda x:(-x[1], x[0]))
    res = []
    for i in range(N):
        res.append(answer[i][0])
    return res