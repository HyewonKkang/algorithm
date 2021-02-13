N, M = map(int, input().split())
dbj = {}
never = []
for _ in range(N+M):
    name = input()
    if name in dbj:
        dbj[name] += 1
    else:
        dbj[name] = 1
for name in dbj:
    if dbj[name] > 1:
        never.append(name)
print(len(never))
never.sort()
for i in never:
    print(i)