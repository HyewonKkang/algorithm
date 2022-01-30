import sys
N = int(sys.stdin.readline())
tree = [[] for _ in range((N + 1))]
visited = [False] * (N + 1)
sys.setrecursionlimit(1000000)

res = [0 for i in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

for i in tree:
    i.sort()


def dfs(v):
    visited[v] = True
    for i in tree[v]:
        if not visited[i]:
            res[i] = v
            dfs(i)


dfs(1)
for i in range(2, N + 1):
    print(res[i])