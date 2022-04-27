from collections import deque
def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    rows = {i : [i - 1, i + 1] for i in range(n)}
    rows[0] = [-1, 1]
    rows[n - 1] = [n - 2, -1]
    restore = deque([])
    chosen = k
    for command in cmd:
        commands = command.split()
        if commands[0] == 'U':
            for _ in range(int(commands[1])):
                chosen = rows[chosen][0]
        elif commands[0] == 'D':
            for _ in range(int(commands[1])):
                chosen = rows[chosen][1]
        elif commands[0] == 'C':
            prev, next = rows[chosen]
            answer[chosen] = 'X'
            restore.append([prev, chosen, next])
            if next == -1:
                chosen = rows[chosen][0]
            else:
                chosen = rows[chosen][1]
            if prev == -1:
                rows[next][0] = -1
            elif next == -1:
                rows[prev][1] = -1
            else:
                rows[prev][1] = next
                rows[next][0] = prev
        elif commands[0] == 'Z':
            prev, now, next = restore.pop()
            answer[now] = 'O'
            if prev == -1:
                rows[next][0] = now
            elif next == -1:
                rows[prev][1] = now
            else:
                rows[next][0] = now
                rows[prev][1] = now

    return ''.join(answer)
