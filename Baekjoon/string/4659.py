case = []
pwd = ''
vowels = ['a', 'e', 'i', 'o', 'u']
while True:
    pwd = input()
    if pwd == 'end': break
    flag = 1
    stack = []
    vowel_cnt = 0
    cont_vowel, cont_constant = 0, 0
    for alphabet in pwd:
        if alphabet in vowels:
            vowel_cnt += 1
            cont_vowel += 1
            cont_constant = 0
        else:
            cont_constant += 1
            cont_vowel = 0
        if cont_constant >= 3 or cont_vowel >= 3:
            flag = 0
            break
        if stack and stack[-1] == alphabet:
            if alphabet == 'e' or alphabet == 'o':
                pass
            else:
                flag = 0
                break
        stack.append(alphabet)

    if vowel_cnt == 0:
        flag = 0

    if flag == 1:
        print('<' + pwd + '> is acceptable.')
    else:
        print('<' + pwd + '> is not acceptable.')