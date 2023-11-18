from collections import deque
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    durations = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    dp = [0] * (n + 1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())

    def topology_sort():
        q = deque([])

        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = durations[i]

        while q:
            now = q.popleft()

            for i in graph[now]:
                indegree[i] -= 1
                dp[i] = max(dp[now] + durations[i], dp[i])
                if indegree[i] == 0:
                    q.append(i)


    topology_sort()
    print(dp[w])