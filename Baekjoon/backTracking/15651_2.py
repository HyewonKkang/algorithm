N, M = map(int, input().split())
check = [False] * (N+1) # 중복숫자 체크
stack = [0] * M

def dfs(cnt):
    if cnt == M:
        for i in stack:
            print(i, end = ' ')
        print()
        return

    for i in range(1, N+1):
        check[i] = True
        stack[cnt] = i
        dfs(cnt+1)
        check[i] = False

dfs(0)