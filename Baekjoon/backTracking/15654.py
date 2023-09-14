n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def backtracking(arr):
    if len(arr) == m:
        print(' '.join(arr))
        return

    for n in nums:
        if str(n) not in arr:
            arr.append(str(n))
            backtracking(arr)
            arr.pop()

backtracking([])