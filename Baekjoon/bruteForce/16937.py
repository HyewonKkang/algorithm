h, w = map(int, input().split())
n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))

if n < 2: print(0)
else:
    max_area = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            r1, c1 = arr[i][0], arr[i][1]
            r2, c2 = arr[j][0], arr[j][1]
            area = r1 * c1 + r2 * c2
            if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
                max_area = max(max_area, area)
            elif (r1 + c2 <= h and max(r2, c1) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
                max_area = max(max_area, area)
            elif (r1 + r2 <= w and max(c1, c2) <= h) or (max(r1, r2) <= w and c1 + c2 <= h):
                max_area = max(max_area, area)
            elif (r1 + c2 <= w and max(r2, c1) <= h) or (max(r1, c2) <= w and c1 + r2 <= h):
                max_area = max(max_area, area)
    print(max_area)