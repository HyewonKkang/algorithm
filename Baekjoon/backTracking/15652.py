n, m = map(int, input().split())

def backtracking(arr, idx):
    if len(arr) == m:
        print(' '.join(arr))
        return
    for i in range(idx, n + 1):
        arr.append(str(i))
        backtracking(arr, i)
        arr.pop()


backtracking([], 1)