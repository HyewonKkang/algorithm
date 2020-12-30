from itertools import combinations

while True:
    S = map(int, input().split())
    lotto = list(S)

    if lotto.pop(0) == 0:
        break

    for i in list(combinations(lotto, 6)):
        for j in i:
            print(j, end=" ")
        print()
    print()
