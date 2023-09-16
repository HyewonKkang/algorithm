n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def countBroken():
    tmp = 0
    for egg in eggs:
        if egg[0] <= 0:
            tmp += 1
    return tmp

def backtracking(cur):
    global answer
    if cur == n:
        answer = max(answer, countBroken())
        return

    if eggs[cur][0] <= 0:
        backtracking(cur + 1)
        return
    if countBroken() == n - 1:
        backtracking(cur + 1)
        return
    for i in range(n):
        if cur == i or eggs[i][0] <= 0: continue
        eggs[cur][0] -= eggs[i][1]
        eggs[i][0] -= eggs[cur][1]
        backtracking(cur + 1)
        eggs[cur][0] += eggs[i][1]
        eggs[i][0] += eggs[cur][1]

backtracking(0)
print(answer)
