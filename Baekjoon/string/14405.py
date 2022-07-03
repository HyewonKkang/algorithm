s = input()
i = 0
length = len(s)
flag = 1
while i < length:
    if s[i:i+2] == 'pi' or s[i:i+2] == 'ka':
        i += 2
    elif s[i:i+3] == 'chu':
        i += 3
    else:
        flag = 0
        break
if flag == 1: print("YES")
else: print("NO")