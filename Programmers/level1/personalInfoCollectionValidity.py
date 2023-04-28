def getDatetime(date):
    tmp = list(map(int, date.split('.')))
    return tmp[0] * (28 * 12) + tmp[1] * 28 + tmp[2]


def solution(today, terms, privacies):
    answer = []
    todayDatetime = getDatetime(today)
    terms = {t: int(m) for t, m in [term.split() for term in terms]}
    for i, privacy in enumerate(privacies):
        date, type = privacy.split()
        datetime = getDatetime(date)
        diff = todayDatetime - datetime
        if diff >= terms[type] * 28:
            answer.append(i + 1)
    return answer

