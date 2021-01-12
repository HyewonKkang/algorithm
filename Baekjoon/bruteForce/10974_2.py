N = int(input())
check = [False] * (N+1)
stack = [0] * N
nums = [i for i in range(1, N+1)]

def dfs(idx):
    if idx == N:
        for i in stack:
            print(i, end = ' ')
        print()
        return

    for i in range(1, N+1):
        if check[i]:
            continue
        check[i] = True
        stack[idx] = i
        dfs(idx + 1)
        check[i] = False

dfs(0)