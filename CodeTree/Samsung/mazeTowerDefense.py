# 미로 타워 디펜스
from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
rounds = [list(map(int, input().split())) for _ in range(m)]
answer = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
traversal = [(0, -1), (1, 0), (0, 1), (-1, 0)]
center = (n // 2, n // 2)

def getNumbers():
    d = 0
    x, y = center
    numbers = []
    next_count = 1
    count = 0
    repeat = 0
    while True:
        nx, ny = x + traversal[d % 4][0], y + traversal[d % 4][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= n: break
        count += 1
        if grid[nx][ny]: numbers.append(grid[nx][ny])
        if count == next_count:
            d += 1
            count = 0
            repeat += 1
        if repeat == 2:
            next_count += 1
            repeat = 0
            count = 0
        x, y = nx, ny
    return numbers

def putNumbers(numbers):
    global grid
    grid = [[0] * n for _ in range(n)]
    numbers = deque(numbers)
    d = 0
    x, y = center
    next_count = 1
    count = 0
    repeat = 0
    while numbers:
        nx, ny = x + traversal[d % 4][0], y + traversal[d % 4][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= n: break
        count += 1
        grid[nx][ny] = numbers.popleft()
        if count == next_count:
            d += 1
            count = 0
            repeat += 1
        if repeat == 2:
            next_count += 1
            repeat = 0
            count = 0
        x, y = nx, ny

def zipCounter(numbers):
    global answer
    last = [numbers[0], 1]
    result = []
    for num in numbers[1:]:
        if num == last[0]:
            last[1] += 1
        else:
            if last[1] < 4:
                result.append(last)
            else:
                answer += last[0] * last[1]
            last = [num, 1]
    if last[1] < 4:
        result.append(last)
    else:
        answer += last[0] * last[1]
    return result

def unzipCounter(counter):
    result = []
    for c in counter:
        num, count = c
        for _ in range(count):
            result.append(num)
    return result


for attack in rounds:
    d, p = attack
    x, y = center
    dx, dy = directions[d]
    for _ in range(p):
        x, y = x + dx, y + dy
        answer += grid[x][y]
        grid[x][y] = 0

    prev = getNumbers()
    while True:
        counter = zipCounter(prev)
        unZipped = unzipCounter(counter)
        if prev == unZipped:
            break
        prev = unZipped
    putNumbers(unZipped)

    counter = zipCounter(unZipped)
    new_numbers = []
    for c in counter:
        num, count = c
        new_numbers.append(count)
        new_numbers.append(num)

    putNumbers(new_numbers)

print(answer)