n, m = map(int, input().split())
answer = []
def backtracking(arr, idx):
    if len(arr) == m:
        print(' '.join(arr))
        return
    for i in range(1, n + 1):
        arr.append(str(i))
        backtracking(arr, idx + 1)
        arr.pop()


backtracking([], 1)