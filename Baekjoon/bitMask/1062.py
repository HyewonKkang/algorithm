from collections import deque
from itertools import combinations
N, K = map(int, input().split())
alphabets = ['a', 'n', 't', 'i', 'c']
K -= 5
new_list = []
answer = 0
for i in range(N):
    if K < 1:
        break
    dq = deque()
    input_ = input()
    list_ = list(input_)
    for k in list_:
        dq.append(k)
    for _ in range(3):
        dq.popleft()
        dq.pop()
    cnt = len(dq)
    for letter in list(dq):
        if letter in alphabets:
            dq.remove(letter)
    str = ''
    for a in dq:
        str += a
    new_list.append(str)

new_list.sort(key=len)

remainder = {'b':0,'d':0,'e':0,'f':0,'g':0,'h':0,
             'j':0,'k':0,'l':0,'m':0,'o':0,'p':0,
             'q':0,'r':0,'s':0,'u':0,'v':0,'w':0,
             'x':0,'y':0,'z':0}
letters = []
for i in list(combinations(remainder, K)):
    for j in i:
        if j in new_list:



print(answer)
