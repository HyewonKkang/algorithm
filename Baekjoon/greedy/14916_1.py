n = int(input())
changes = [0, 0]
answer = -1

if n >= 2:
    while n >= 5:
        n -= 5
        changes[0] += 1
    while n >= 2:
        n -= 2
        changes[1] += 1
    if n > 0 and changes[0] > 0:
        changes[0] -= 1
        n += 5
        while n != 0:
            n -= 2
            changes[1] += 1

if n != 0:
    answer = -1
else:
    if changes[0] != 0 or changes[1] != 0:
        answer = changes[0] + changes[1]

print(answer)


