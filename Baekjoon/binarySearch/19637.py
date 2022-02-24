import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
titles = []
for _ in range(N):
    name, value = map(str, sys.stdin.readline().rstrip().split())
    titles.append([name, int(value)])
for _ in range(M):
    power = int(sys.stdin.readline().rstrip())
    start = 0
    end = N - 1
    res = ''
    flag = 0
    while start <= end:
        mid = (start + end) // 2
        if titles[mid][1] >= power:
            end = mid - 1
        elif titles[mid][1] < power:
            start = mid + 1
    print(titles[start][0])
