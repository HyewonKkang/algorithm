def solution(n, results):
    answer = 0
    win = {i: [] for i in range(1, n + 1)}
    lose = {i: [] for i in range(1, n + 1)}
    for res in results:
        a, b = res
        win[a].append(b)
        lose[b].append(a)

    def dfs(graph, player):
        stack = [player]
        visited = [False] * (n + 1)
        while stack:
            val = stack.pop()
            visited[val] = True
            for other in graph[val]:
                if not visited[other]:
                    stack.append(other)

        return sum(visited)

    for i in range(1, n + 1):
        answer += dfs(win, i) + dfs(lose, i) == n + 1

    return answer
