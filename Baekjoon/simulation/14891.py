from collections import deque
gears = [deque()] + [deque(map(int, list(input()))) for _ in range(4)]
k = int(input())
rotations = [list(map(int, input().split())) for _ in range(k)]

for r in rotations:
    cur, direction = r
    dirs = [0, 0, 0, 0, 0]
    dirs[cur] = direction
    compareSet = [(0, 0)] + [(gears[i][6], gears[i][2]) for i in range(1, 5)]
    gears[cur].rotate(direction)

    # check left side
    for i in range(cur - 1, -1, -1):
        if compareSet[i][1] == compareSet[i + 1][0]:
            break
        gears[i].rotate(-dirs[i + 1])
        dirs[i] = -dirs[i + 1]

    # check right side
    for i in range(cur + 1, 5):
        if compareSet[i - 1][1] == compareSet[i][0]:
            break
        gears[i].rotate(-dirs[i - 1])
        dirs[i] = -dirs[i - 1]

print(gears[1][0] * 1 + gears[2][0] * 2 + gears[3][0] * 4 + gears[4][0] * 8)
