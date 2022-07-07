import sys
n = int(input())
options = []
shortcut_keys = []
print_keys = []
for i in range(n):
    option = sys.stdin.readline().rstrip()
    options.append(option)
    option_arr = option.split()
    string = ''
    flag = 0
    key = ''
    for i in range(len(option_arr)):
        if i != 0: string += ' '
        if flag == 0 and option_arr[i][0].upper() not in shortcut_keys and option_arr[i][0].lower() not in shortcut_keys:
            string += '[' + option_arr[i][0] + ']' + option_arr[i][1:]
            flag = 1
            key = option_arr[i][0]
        else:
            string += option_arr[i]
    if flag == 1:
        shortcut_keys.append(key)
        print_keys.append(string)
        continue

    string = ''
    flag = 0
    key = ''
    for i in range(len(option)):
        if option[i] == ' ':
            string += option[i]
            continue
        if flag == 0 and option[i].upper() not in shortcut_keys and option[i].lower() not in shortcut_keys:
            string += '[' + option[i][0] + ']' + option[i][1:]
            flag = 1
            key = option[i][0]
        else:
            string += option[i]

    if flag == 1:
        shortcut_keys.append(key)
        print_keys.append(string)
        continue
    else:
        shortcut_keys.append(' ')
        print_keys.append(string)
for option in print_keys:
    print(option)