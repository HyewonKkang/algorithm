resistance = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
answer = ''
input_color = input()
for i in range(len(resistance)):
    if input_color == resistance[i]:
        answer += str(i)
        break
input_color = input()
for i in range(len(resistance)):
    if input_color == resistance[i]:
        answer += str(i)
        break
input_color = input()
answer = int(answer)
for i in range(len(resistance)):
    if input_color == resistance[i]:
        answer *= 10**i
print(answer)