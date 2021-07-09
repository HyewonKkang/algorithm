def solution(files):
    answer = []
    head = []
    number = []
    tail = []
    fileList = []

    for file in files:
        num_start = 0
        for i in range(1, len(file)):
            if file[i].isdigit():
                if not file[i - 1].isdigit():
                    head.append(file[:i])
                    num_start = i
                if i != len(file)-1:
                    if not file[i + 1].isdigit():
                        number.append(file[num_start:i + 1])
                        tail.append(file[i + 1:])
                        break
                else:
                    number.append(file[num_start:i + 1])
                    tail.append('')

    for pair in zip(head, number, tail):
        fileList.append(list(pair))

    fileList.sort(key=lambda x:int(x[1]))
    fileList.sort(key=lambda x:x[0].lower())

    for file in fileList:
        answer.append(file[0] + file[1] + file[2])

    return answer