import sys

S = list(sys.stdin.readline().rstrip())
start = 0
i = 0

while i < len(S):
    if S[i] == '<':
        i += 1
        while S[i] != '>':
            i += 1
        i += 1
    elif 'a' <= S[i] <= 'z' or '0' <= S[i] <= '9':
        start = i
        while i < len(S):
            if S[i] == ' ' or S[i] == '>' or S[i] == '<':
                break
            i += 1
        tmp = S[start:i]
        S[start:i] = tmp[::-1]
    else:
        i += 1


print(''.join(S))
