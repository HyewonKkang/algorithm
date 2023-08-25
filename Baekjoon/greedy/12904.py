s, t = list(input()), list(input())
flag = 0

while t and t != s:
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()
    if s == t:
        flag = 1

print(flag)