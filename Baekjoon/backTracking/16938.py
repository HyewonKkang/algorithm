n, l, r, x = map(int, input().split())
difficulties = list(map(int, input().split()))
visited = [False] * n
answer = 0

def backtracking(arr, visited, idx):
    global answer
    if l <= sum(arr) <= r and max(arr) - min(arr) >= x:
        answer += 1
    if sum(arr) > r:
        return

    for i in range(idx, len(difficulties)):
        if not visited[i]:
            visited[i] = True
            backtracking(arr + [difficulties[i]], visited, i + 1)
            visited[i] = False


backtracking([], visited, 0)
print(answer)
