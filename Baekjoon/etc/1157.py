word = input().lower()
alphabets = [0] * 26
for letter in word:
    alphabets[ord(letter)-97] += 1
max = 0
max_index = 0
flag = 0
for i in range(len(alphabets)):
    if max < alphabets[i]:
        max = alphabets[i]
        max_index = i
        flag = 0
    elif max == alphabets[i]:
        flag = 1
if flag == 1:
    print("?")
else:
    print(chr(max_index + 97).upper())