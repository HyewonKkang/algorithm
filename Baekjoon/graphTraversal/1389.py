from collections import deque
n, m = map(int, input().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

kevinBacon = [int(1e9)]

def bfs(v):
    visited = [False] * (n + 1)
    q = deque([v])
    nums = [0] * (n + 1)
    visited[v] = True
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                nums[i] = nums[cur] + 1
                q.append(i)
                visited[i] = True
    return sum(nums)


for v in range(1, n + 1):
    kevinBacon.append(bfs(v))

print(kevinBacon.index(min(kevinBacon)))