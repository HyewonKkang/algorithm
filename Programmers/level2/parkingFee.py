import math
def calcTime(arr):
    total_minutes = 0
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):
            out_h, out_m = arr[i + 1][0], arr[i + 1][1]
        else:
            out_h, out_m = 23, 59
        in_h, in_m = arr[i][0], arr[i][1]
        total_minutes += (out_h * 60 + out_m) - (in_h * 60 + in_m)

    return total_minutes

def solution(fees, records):
    answer = {}
    record = {}
    for r in records:
        tmp = r.split(' ')
        h, m = map(int, tmp[0].split(':'))
        if tmp[1] in record:
            record[tmp[1]].append([h, m, tmp[2]])
        else:
            record[tmp[1]] = [[h, m, tmp[2]]]

    for car in record:
        parkedTime = calcTime(record[car])
        if parkedTime < fees[0]:
            answer[car] = fees[1]
        else:
            answer[car] = fees[1] + math.ceil((parkedTime - fees[0]) / fees[2]) * fees[3]

    res = []
    dict = sorted(answer.items())
    for d in dict:
        res.append(d[1])
    return res
