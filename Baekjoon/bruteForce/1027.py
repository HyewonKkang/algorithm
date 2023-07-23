n = int(input())
buildings = list(map(int, input().split()))
answer = 0


def calcSlope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


for i, cur in enumerate(buildings):
    count = 0
    min_slope = int(1e9)
    max_slope = -int(1e9)

    for left_index in range(i-1, -1, -1):
        slope = calcSlope(left_index, buildings[left_index], i, cur)
        if slope < min_slope:
            min_slope = slope
            count += 1
    for right_index in range(i+1, n):
        slope = calcSlope(right_index, buildings[right_index], i, cur)
        if slope > max_slope:
            max_slope = slope
            count += 1
    answer = max(answer, count)

print(answer)