from collections import defaultdict
import math

def calcTime(s, e='23:59'):
    sh, sm = list(map(int, s.split(':')))
    eh, em = list(map(int, e.split(':')))
    return (eh - sh) * 60 + (em - sm)

def solution(fees, records):
    answer = []
    basicTime, basicFee, unitTime, unitFee = fees
    times = defaultdict(int)
    cars = defaultdict(list)

    def calcFee(time):
        if time <= basicTime: return basicFee
        return basicFee + math.ceil((time - basicTime) / unitTime) * unitFee

    for r in records:
        time, car, type = r.split(' ')
        if type == 'IN':
            cars[car].append(time)
        else:
            times[car] += calcTime(cars[car].pop(), time)

    for car, val in cars.items():
        if val: times[car] += calcTime(val[0])

    sortedTime = sorted(times.items(), key=lambda x:x[0])
    answer = [calcFee(time[1]) for time in sortedTime]

    return answer
