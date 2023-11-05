import heapq
i = 0
while True:
    n = int(input())
    if n == 0: break
    arr = [list(map(int, input().split())) for _ in range(n)]
    distance = [[int(1e9)] * n for _ in range(n)]
    distance[0][0] = arr[0][0]

    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    while q:
        val, x, y = heapq.heappop(q)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = val + arr[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    i += 1

    problem_number = i
    result_distance = distance[n - 1][n - 1]
    print(f'Problem {problem_number}: {result_distance}')


