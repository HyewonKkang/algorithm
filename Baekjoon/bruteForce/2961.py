from itertools import combinations
n = int(input())
arr = []
for _ in range(n):
    s, b = map(int, input().split())
    arr.append([s, b])
differences = []
for i in range(1, n + 1):
    for sets in list(combinations(arr, i)):
        s_total = 1
        b_total = 0
        for ingredient in sets:
            s_total *= ingredient[0]
            b_total += ingredient[1]
        differences.append(abs(s_total - b_total))
print(min(differences))