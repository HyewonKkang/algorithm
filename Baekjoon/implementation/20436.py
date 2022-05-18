keyboards = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

sl, sr = input().split()
string = input()
left, right = 0, 0
keyboard_dict = {}

for i in range(3):
    for j in range(len(keyboards[i])):
        keyboard_dict[keyboards[i][j]] = (i, j)

left, right = keyboard_dict[sl], keyboard_dict[sr]
times = 0

for s in string:
    sl, sr = keyboard_dict[s]
    if (sl <= 1 and sr <= 4) or (sl == 2 and sr <= 3):
        times += abs(sl - left[0]) + abs(sr - left[1])
        left = keyboard_dict[s]
    else:
        times += abs(sl - right[0]) + abs(sr - right[1])
        right = keyboard_dict[s]
    times += 1

print(times)