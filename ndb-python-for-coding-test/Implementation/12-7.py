N = list(map(int, input()))
length = len(N)
left, right = N[0:length // 2], N[length // 2:length]
if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")