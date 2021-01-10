dwarfs = list()
for i in range(9):
    n = int(input())
    dwarfs.append(n)
dwarfs.sort()
total = sum(dwarfs)
out_val = 0
for i in range(8):
    for j in range(i+1, 9):
        if total - (dwarfs[i] + dwarfs[j]) == 100:
            for k in range(9):
                if i == k or j == k:
                    continue
                else:
                    print(dwarfs[k])
            out_val = 1
    if out_val == 1:
        break