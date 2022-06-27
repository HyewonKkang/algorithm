str = input()
sounds = {'q':0, 'u':0, 'a':0, 'c':0, 'k':0}
sounds_idx = ['q', 'u', 'a', 'c', 'k']
dup = 0
cnt = 0
for s in str:
    if s == 'q':
        sounds[s] += 1
    else:
        s_index = sounds_idx.index(s)
        if sounds[sounds_idx[s_index - 1]] < sounds[sounds_idx[s_index]] + 1:
            dup = -1
            break
        else:
            sounds[sounds_idx[s_index]] += 1
            if s == 'k':
                if sounds['q'] != sounds['k']:
                    dup = max(sounds['q'] - sounds['k'] + 1, dup)
if dup == -1:
    print(-1)
else:
    flag = 0
    t = sounds['q']
    for s in sounds:
        if sounds[s] != t:
            print(-1)
            flag = 1
            break
    if flag == 0:
        if dup == 0:
            print(1)
        else:
            print(dup)
