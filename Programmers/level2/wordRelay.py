def solution(n, words):
    answer = []
    wordsList = []
    numOfPerson = 0
    order = 0

    idx = 0
    for i in range(len(words)):
        if len(wordsList) == 0:
            wordsList.append(words[i])
        else:
            if words[i] not in wordsList:
                if words[i].startswith(wordsList[-1][-1]):
                    wordsList.append(words[i])
                else:
                    idx = i
                    break
            else:
                idx = i
                break

    if idx != 0:
        numOfPerson = idx % n + 1
        order = idx // n + 1
    answer.append(numOfPerson)
    answer.append(order)
    return answer
