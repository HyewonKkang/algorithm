from itertools import combinations
n, m = map(int, input().split())
preferences = [list(map(int, input().split())) for _ in range(n)]
chickens = [i for i in range(m)]

max_total = 0
for chicken_set in list(combinations(chickens, 3)):
    total = 0
    for preference in preferences:
        person = 0
        for i in chicken_set:
            person = max(person, preference[i])
        total += person
    max_total = max(max_total, total)
print(max_total)