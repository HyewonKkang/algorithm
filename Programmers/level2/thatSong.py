def subTime(start, end):
    start_hour, start_min = map(int, start.split(':'))
    end_hour, end_min = map(int, end.split(':'))
    total_min = (60 * end_hour + end_min) - (60 * start_hour + start_min)
    return total_min

def getScore(sc):
    score = []
    for i in range(len(sc) - 1):
        if sc[i] == '#': continue
        if sc[i + 1] == '#':
            score.append(sc[i:i + 2])
        else:
            score.append(sc[i])
    if sc[len(sc) - 1] != '#':
        score.append(sc[len(sc) - 1])
    return score


def solution(m, musicinfos):
    answer = '(None)'
    res = []
    for music in musicinfos:
        tmp = music.split(',')
        length = subTime(tmp[0], tmp[1])
        title, score = tmp[2], getScore(tmp[3])

        song = []
        i = 0
        origin_len = len(score)
        while len(song) != length:
            song.append(score[i % origin_len])
            i += 1

        melody = getScore(m)

        for i in range(len(song)):
            if melody[0] == song[i]:
                k = 0
                if len(song[i+k:]) < len(melody): break
                while melody[k] and song[i + k]:
                    if melody[k] != song[i + k]:
                        break
                    k += 1
                    if k == len(melody):
                        res.append((title, length))
                        break


    if len(res) == 0:
        return answer
    elif len(res) >= 1:
        res.sort(key=lambda x:-x[1])
    return res[0][0]



print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))