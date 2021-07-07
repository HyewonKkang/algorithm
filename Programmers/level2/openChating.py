def solution(record):
    answer = []
    logs = []
    dict = {}

    for log in record:
        logs.append(log.split(' '))

    for log in logs:
        if log[0] == 'Enter':
            dict[log[1]] = log[2]
        elif log[0] == 'Change':
            dict[log[1]] = log[2]

    for log in logs:
        if log[0] == 'Enter':
            answer.append(dict[log[1]] + "님이 들어왔습니다.")
        elif log[0] == 'Leave':
            answer.append(dict[log[1]] + "님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))