from collections import deque
N, K = map(int, input().split())
alphabets = ['a', 'n', 't', 'i', 'c']
new_list = []
answer = 0
for i in range(K):
    if K < 5:
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
        if a not in new_list:
            str += a
    new_list.append(str)

remainder = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
nums = [0] * 21
idx = 0
while True:
    if len(new_list) == 0:
        break
    # if new_list[idx] == ' ':



print(answer)
