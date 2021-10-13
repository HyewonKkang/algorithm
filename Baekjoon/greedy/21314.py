def convertNum1(str_list):
    result = ''
    for str in str_list:
        if 'K' in str:
            result += '5'
            cnt = str.count('M')
            for i in range(cnt):
                result += '0'
        else:
            cnt = str.count('M')
            result += '1'
            for i in range(cnt - 1):
                result += '1'
    print(result)

def convertNum2(str_list):
    result = ''
    for str in str_list:
        if 'K' in str:
            result += '5'
            cnt = str.count('M')
            for i in range(cnt):
                result += '0'
        else:
            cnt = str.count('M')
            result += '1'
            for i in range(cnt - 1):
                result += '0'
    print(result)

string = input()

# find largest
new = ''
str_list = []
for letter in string:
    new += letter
    if letter == 'K':
        str_list.append(new)
        new = ''
if new != '':
    str_list.append(new)
convertNum1(str_list)

# find smallest
new = ''
str_list = []
for letter in string:
    if letter == 'K':
        if new != '':
            str_list.append(new)
        str_list.append(letter)
        new = ''
    else:
        new += letter
if new != '':
    str_list.append(new)
convertNum2(str_list)