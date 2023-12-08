def getTime(time):
    s_h, s_m = map(int, time[0].split(':'))
    e_h, e_m = map(int, time[1].split(':'))
    return [s_h * 60 + s_m, e_h * 60 + e_m]


def solution(book_time):
    answer = 0
    times = []
    for time in book_time:
        times.append(getTime(time))
    ends = []

    times.sort(key=lambda x: (x[0], x[1]))
    for time in times:
        start, end = time
        for i, e in enumerate(ends):
            if e + 10 <= start:
                ends[i] = end
                break
        else:
            ends.append(end)

    return len(ends)
