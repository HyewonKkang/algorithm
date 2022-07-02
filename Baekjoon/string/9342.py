import sys
t = int(input())
for _ in range(t):
    string = sys.stdin.readline().rstrip()
    flag = 0
    string = string[1:]
    a_idx = string.find('A')
    f_idx = string.find('F')
    c_idx = string.find('C')
    if a_idx < f_idx < c_idx:
        flag = 1
    sub = string[c_idx+1:]
    if len(sub) > 1:
        flag = 0
    for s in sub:
        if s not in ['A', 'B', 'C', 'D', 'E', 'F']:
            flag = 0
            break

    if not flag:
        print("Good")
    else:
        print("Infected!")
