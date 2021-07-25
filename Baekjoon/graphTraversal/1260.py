from collections import deque
import sys
def printRes(list):
    for i in list:
        print(i, end = ' ')

def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            list_ = []
            for v in graph[n]:
                if v not in visited:
                    list_.append(v)
            list_.sort(reverse=True)
            stack.extend(list_)
    printRes(visited)

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        list_ = []
        for v in graph[n]:
            if v not in visited:
                list_.append(v)
        list_.sort()
        queue.extend(list_)
        if n not in visited:
            visited.append(n)
    printRes(visited)

N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    if n1 not in graph[n2]:
        graph[n2].append(n1)
    if n2 not in graph[n1]:
        graph[n1].append(n2)
dfs(graph, V)
print()
bfs(graph, V)