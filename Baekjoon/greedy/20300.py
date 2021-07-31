from collections import deque

N = int(input())
lossOfMuscle = list(map(int, input().split()))
lossOfMuscle.sort()
lossOfMuscle = deque(lossOfMuscle)
totals = []

if len(lossOfMuscle) % 2 != 0:
    totals.append(lossOfMuscle.pop())

while len(lossOfMuscle) > 0:
        totals.append(lossOfMuscle.popleft() + lossOfMuscle.pop())

lossOfMuscle = list(totals)
totals.sort()
print(totals[-1])
