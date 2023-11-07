t = int(input())


def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for _ in range(t):
    n, m = map(int, input().split())

    parents = [i for i in range(n + 1)]
    result = 0

    for edge in range(m):
        a, b = map(int, input().split())
        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
            result += 1
    print(result)