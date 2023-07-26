from itertools import combinations
l, c = map(int, input().split())
passwords = sorted(list(input().split()))
answer = []
vowels = ['a', 'e', 'i', 'o', 'u']
for pwd in list(combinations(passwords, l)):
    c_count, v_count = 0, 0
    for p in pwd:
        if p in vowels: v_count += 1
        else: c_count += 1
    if v_count >= 1 and c_count >= 2:
        answer.append(''.join(pwd))
for ans in answer:
    print(''.join(ans))