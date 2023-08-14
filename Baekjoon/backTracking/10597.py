file = input()
answer = []
n = len(file) if len(file) <= 9 else (len(file) - 9) // 2 + 9


def backtracking(idx):
    if len(answer) == n:
        print(' '.join(answer))
        exit(0)
    if file[idx] != '0' and file[idx] not in answer:
        answer.append(file[idx])
        backtracking(idx + 1)
        answer.pop()
    if file[idx] != '0' and int(file[idx:idx+2]) <= n and file[idx:idx+2] not in answer:
        answer.append(file[idx:idx+2])
        backtracking(idx + 2)
        answer.pop()


backtracking(0)