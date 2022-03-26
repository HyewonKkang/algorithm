s = input()
tmp = s[0]
for num in s:
    if num == tmp[len(tmp) - 1]:
        continue
    tmp += num
print(min(tmp.count('0'), tmp.count('1')))
