N = int(input())
M = int(input())
visited = []
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(root, visited=[]):
    visited.append(root)
    for node in graph[root]:
        if node not in visited:
            dfs(node, visited)
    return visited

answer = len(dfs(1, visited)) - 1
print(answer)