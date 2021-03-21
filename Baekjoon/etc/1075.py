N = input()
F = int(input())
num = ''
for i in range(0, len(N)-2):
    num += N[i]
num += '00'
N = int(num)
while True:
    if N % F == 0:
        break
    else:
        N += 1
answer = str(N)[-2:]
print(answer)