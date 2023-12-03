from collections import deque

def solution(n, computers):
    answer = 0
    networks = {i:[] for i in range(n)}
    visited = [False] * n

    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j]:
                networks[i].append(j)

    def bfs(i):
        q = deque([i])
        visited[i] = True
        while q:
            node = q.popleft()
            for neighbor in networks[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
        return True

    for i in range(n):
        if not visited[i]:
            answer += bfs(i)
    return answer
