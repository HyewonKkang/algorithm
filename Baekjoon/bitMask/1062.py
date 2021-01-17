# 메모리 초과,,,
# 파이썬으로는 풀 수 없는 문제인 것인가,,,, - from google,,,
# 다음에 c++로 풀어볼 것,,,,
from itertools import combinations
from sys import stdin
N, K = map(int, stdin.readline().split())
alphabets = ['a', 'n', 't', 'i', 'c']
K -= 5
new_list = []
letters = []
answer = []
failure = 0; result = 0
for i in range(N):
    if K < 1:
        failure = 1
        break
    input_ = stdin.readline()[4:-5]
    list_ = list(input_)
    str = ''
    for letter in list_:
        if letter not in alphabets:
            letters.append(letter)
            str += letter
    new_list.append(str)

if failure == 1:
    pass
else:
    for subset in list(combinations(letters, K)):
        cnt_ = 0
        cnt = [0] * N
        for i in range(len(subset)):
            for j in range(N):
                cnt[j] += new_list[j].count(subset[i])
        for i in range(N):
            if cnt[i] == len(new_list[i]):
                cnt_ += 1
        if result < cnt_:
            result = cnt_
print(result)
