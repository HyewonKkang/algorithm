import sys
def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(graph[n])
    return visited


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n2].append(n1)
    graph[n1].append(n2)

nums = [i for i in range(1, N+1)]
connected = []
lists = []
cnt = 0
for i in range(1, N + 1):
    if i not in lists:
        connected = dfs(graph, i)
        lists.extend(connected)
        cnt = cnt + 1

print(cnt)
