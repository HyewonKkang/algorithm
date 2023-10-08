import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def findNear(prevs):
    tmp = []
    for prev in prevs:
        x, y = prev
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in prevs:
                tmp.append((nx, ny))
    return tmp


for i in range(n):
    for j in range(m):
        one = (i, j)
        second = findNear([one])
        for pt1 in second:
            two = (pt1[0], pt1[1])
            third = findNear([one, two])
            for pt2 in third:
                three = (pt2[0], pt2[1])
                fourth = findNear([one, two, three])
                for pt3 in fourth:
                    four = (pt3[0], pt3[1])
                    total = board[one[0]][one[1]] + board[two[0]][two[1]] + board[three[0]][three[1]] + board[four[0]][four[1]]
                    answer = max(answer, total)

print(answer)

