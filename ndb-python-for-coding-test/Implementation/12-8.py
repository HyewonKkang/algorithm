from collections import deque
s = list(input())
s.sort()
q = deque(s)
total = 0
while q:
    if '0' <= q[0] <= '9':
        total += int(q.popleft())
    else:
        break
print(''.join(list(q)), end='')
print(total)