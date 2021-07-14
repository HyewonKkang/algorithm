def putZero(num):
    if len(num) == 1:
        return '0' + num
    return num

now = list(map(int, input().split(':')))
throw = list(map(int, input().split(':')))
wait = []

# seconds
if now[2] <= throw[2]:
    second = throw[2] - now[2]
else:
    if throw[1] == 0:
        throw[0] -= 1
        throw[1] += 59
    else:
        throw[1] -= 1
    throw[2] += 60
    second = throw[2] - now[2]

# minutes
if now[1] <= throw[1]:
    minute = throw[1] - now[1]
else:
    throw[0] -= 1
    throw[1] += 60
    minute = throw[1] - now[1]

# hours
if now[0] <= throw[0]:
    hour = throw[0] - now[0]
else:
    hour = (12 + throw[0]) - (now[0] - 12)

wait.append(putZero(str(hour)))
wait.append(putZero(str(minute)))
wait.append(putZero(str(second)))

cnt = 0
for time in wait:
    if time == '00':
        cnt += 1
if cnt == 3:
    wait[0] = '24'

answer = ':'.join(wait)
print(answer)