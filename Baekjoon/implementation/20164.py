from collections import Counter

def countOddNums(n):
    counter = Counter(n)
    return counter['1'] + counter['3'] + counter['5'] + counter['7'] + counter['9']

N = input()
answers = []

def solve(N, count):
    if len(N) == 1:
        answers.append(count)
        return
    elif len(N) == 2:
        calc = int(N[1]) + int(N[0])
        newN = str(calc)
        solve(newN, count + countOddNums(newN))
    else:
        for i in range(len(N) - 1):
            for j in range(i + 1, len(N) - 1):
                calc = int(N[:i + 1]) + int(N[i + 1:j + 1]) + int(N[j + 1:])
                newN = str(calc)
                newCount = count + countOddNums(newN)
                solve(newN, newCount)

solve(N, countOddNums(N))
print(min(answers), max(answers))