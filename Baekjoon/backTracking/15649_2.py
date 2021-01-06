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
        check[i] = True
        stack[idx] = i 
        DFS(idx+1, N, M) # +1번째 수열을 위해 재귀함수 호출
        check[i] = False

DFS(0, N, M)