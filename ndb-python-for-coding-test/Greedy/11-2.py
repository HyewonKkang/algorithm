s = input()
value = int(s[0])
for i in range(len(s) - 1):
    value = max(value + int(s[i+1]), value * int(s[i+1]))
print(value)