n = int(input())
arr = []

def backtracking(x):
    arr.append(x)
    left = int(str(x)[0])
    for i in range(left+1, 10):
        backtracking(int(str(i) + str(x)))

for i in range(10):
    backtracking(i)

arr.sort()
try:
    print(arr[n])
except:
    print(-1)