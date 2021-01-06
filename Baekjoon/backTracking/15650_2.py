N, M = map(int, input().split())
check = [False] * (N+1) # 중복숫자 체크
stack = [0] * M
def DFS(idx, N, M):
    if idx == M: # 수열 M개를 충족할 경우 출력
        for i in stack:
            print(i, end = ' ')
        print()
        return

    for i in range(1, N+1):
        if check[i]: # 중복인 경우
            continue
        for j in range(i+1):
            check[j] = True
        stack[idx] = i
        DFS(idx+1, N, M)
        for j in range(1, N+1):
            check[j] = False # 다음 수로 넘어가기 전에 전부 초기화
DFS(0, N, M)