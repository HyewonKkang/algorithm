def solution(genres, plays):
    answer = []
    musics = {}
    genre = {}
    for i in range(len(genres)):
        if genres[i] in musics:
            musics[genres[i]].append([i, plays[i]])
            genre[genres[i]] += plays[i]
        else:
            musics[genres[i]] = [[i, plays[i]]]
            genre[genres[i]] = plays[i]

    gn = dict(sorted(genre.items(), key=lambda x:x[1], reverse=True))
    res = {}
    for g in gn:
        res[g] = musics[g]

    for genre, songs in res.items():
        if len(songs) == 1:
            answer.append(songs[0][0])
        else:
            songs.sort(key=lambda x: x[0])
            songs.sort(key=lambda x: -x[1])
            answer.append(songs[0][0])
            answer.append(songs[1][0])

    return answer

